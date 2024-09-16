import numpy as np

# Define the Sphere Function that we want to approximate using the PSO
def sphereFunction(x:np.ndarray) -> float:
    """
    # Description:
        -> Sphere Function used inside the Research Paper [Summation of (x_i)^2, for i in [1, dim(x)]]
    
    := param x: Numpy array with an nth-dimensional shape
    := return: Approximation of the sphere function given a input array
    """
    return np.sum(np.square(x))