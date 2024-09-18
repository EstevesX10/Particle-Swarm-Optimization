# This file consists of a reimplementation of the plot_surface function from the pyswarms.utils.plotters (pyswarms v1.3.0)

import numpy as np
from matplotlib import (animation, cm)
import matplotlib.pyplot as plt
import logging
import multiprocessing as mp
from pyswarms.utils.plotters.formatters import (Designer, Animator)
from pyswarms.utils.reporter import (Reporter)

rep = Reporter(logger=logging.getLogger(__name__))

def my_plot_surface(
    pos_history,
    canvas=None,
    title="Trajectory",
    designer=None,
    mesher=None,
    animator=None,
    mark=None,
    n_processes=None,
    **kwargs
):
    """Plot a swarm's trajectory in 3D

    This is useful for plotting the swarm's 2-dimensional position with
    respect to the objective function. The value in the z-axis is the fitness
    of the 2D particle when passed to the objective function. When preparing the
    position history, make sure that the:

    * first column is the position in the x-axis,
    * second column is the position in the y-axis; and
    * third column is the fitness of the 2D particle

    The :class:`pyswarms.utils.plotters.formatters.Mesher` class provides a
    method that prepares this history given a 2D pos history from any
    optimizer.

    .. code-block:: python

        import pyswarms as ps
        from pyswarms.utils.functions.single_obj import sphere
        from pyswarms.utils.plotters import plot_surface
        from pyswarms.utils.plotters.formatters import Mesher

        # Run optimizer
        options = {'c1':0.5, 'c2':0.3, 'w':0.9}
        optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options)

        # Prepare position history
        m = Mesher(func=sphere)
        pos_history_3d = m.compute_history_3d(optimizer.pos_history)

        # Plot!
        plot_surface(pos_history_3d)

    Parameters
    ----------
    pos_history : numpy.ndarray
        Position history of the swarm with shape
        :code:`(iteration, n_particles, 3)`
    objective_func : callable
        The objective function that takes a swarm of shape
        :code:`(n_particles, 2)` and returns a fitness array
        of :code:`(n_particles, )`
    canvas : (:obj:`matplotlib.figure.Figure`, :obj:`matplotlib.axes.Axes`),
        The (figure, axis) where all the events will be draw. If :code:`None`
        is supplied, then plot will be drawn to a fresh set of canvas.
    title : str, optional
        The title of the plotted graph. Default is `Trajectory`
    mark : tuple, optional
        Marks a particular point with a red crossmark. Useful for marking the
        optima.
    designer : :obj:`pyswarms.utils.formatters.Designer`, optional
        Designer class for custom attributes
    mesher : :obj:`pyswarms.utils.formatters.Mesher`, optional
        Mesher class for mesh plots
    animator : :obj:`pyswarms.utils.formatters.Animator`, optional
        Animator class for custom animation
    n_processes : int
        number of processes to use for parallel mesh point calculation (default: None = no parallelization)
    **kwargs : dict
        Keyword arguments that are passed as a keyword argument to
        :class:`matplotlib.axes.Axes` plotting function

    Returns
    -------
    :class:`matplotlib.animation.FuncAnimation`
        The drawn animation that can be saved to mp4 or other
        third-party tools
    """
    try:
        # Adjust the limits in the Designer class
        if designer is None:
            designer = Designer(
                limits=[(-2, 2), (-2, 2), (-1, 2)],  # Expanded limits for the axes
                label=["x-axis", "y-axis", "z-axis"],
                colormap=cm.viridis,
                title_fontsize=16,  # Adjust the font size
                text_fontsize=12
            )

        # If no Animator class supplied, use defaults
        if animator is None:
            animator = Animator()

        # Get number of iterations
        # If ax is default, then create new plot. Set-up the figure, the
        # axis, and the plot element that we want to animate
        if canvas is None:
            fig, ax = plt.subplots(1, 1, figsize=designer.figsize, subplot_kw={"projection":"3d"})
        else:
            fig, ax = canvas

        n_iters = len(pos_history)

        # Customize plot
        ax.set_title(title, fontsize=designer.title_fontsize)
        ax.set_xlabel(designer.label[0], fontsize=designer.text_fontsize)
        ax.set_ylabel(designer.label[1], fontsize=designer.text_fontsize)
        ax.set_zlabel(designer.label[2], fontsize=designer.text_fontsize)
        ax.set_xlim(designer.limits[0])
        ax.set_ylim(designer.limits[1])
        ax.set_zlim(designer.limits[2])

        # When setting the title, you can adjust the position by using the pad argument
        ax.set_title(title, fontsize=designer.title_fontsize, pad=30)  # Move title up

        # Set a better viewing angle if necessary
        ax.view_init(elev=30, azim=120)  # Adjust these values to get the best view of the plot
        
        # Make a contour map if possible
        if mesher is not None:
            (xx, yy, zz) = _mesh(mesher, n_processes=n_processes)
            ax.plot_surface(
                xx, yy, zz, cmap=designer.colormap, alpha=mesher.alpha
            )

        # Mark global best if possible
        if mark is not None:
            ax.scatter(mark[0], mark[1], mark[2], color="red", marker="x")

        # Put scatter skeleton
        plot = ax.scatter(xs=[], ys=[], zs=[], c="black", alpha=0.6, **kwargs)

        # Do animation
        anim = animation.FuncAnimation(
            fig=fig,
            func=_animate,
            frames=range(n_iters),
            fargs=(pos_history, plot),
            interval=animator.interval,
            repeat=animator.repeat,
            repeat_delay=animator.repeat_delay,
        )
    except TypeError:
        rep.logger.exception("Please check your input type")
        raise
    else:
        return anim


def _animate(i, data, plot):
    """Helper animation function that is called sequentially
    :class:`matplotlib.animation.FuncAnimation`
    """
    current_pos = data[i]
    if np.array(current_pos).shape[1] == 2:
        plot.set_offsets(current_pos)
    else:
        plot._offsets3d = current_pos.T
    return (plot,)


def _mesh(mesher, n_processes=None):
    """Helper function to make a mesh"""
    xlim = mesher.limits[0]
    ylim = mesher.limits[1]
    x = np.arange(xlim[0], xlim[1], mesher.delta)
    y = np.arange(ylim[0], ylim[1], mesher.delta)
    xx, yy = np.meshgrid(x, y)
    xypairs = np.vstack([xx.reshape(-1), yy.reshape(-1)]).T

    # Get z-value

    # Setup Pool of processes for parallel evaluation
    pool = None if n_processes is None else mp.Pool(n_processes)

    if pool is None:
        z = mesher.func(xypairs)
    else:
        results = pool.map(
            mesher.func, np.array_split(xypairs, pool._processes)
        )
        z = np.concatenate(results)

    # Close Pool of Processes
    if n_processes is not None:
        pool.close()

    zz = z.reshape(xx.shape)
    return (xx, yy, zz)