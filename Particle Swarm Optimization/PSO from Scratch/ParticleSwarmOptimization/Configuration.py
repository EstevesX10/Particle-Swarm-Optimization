def loadConfig() -> dict:
    """
    # Description
        -> Simple function that retrives a given configuration to be used inside the PSO Algorithm
    := return: Python Dictionary with the configuration to be used
    """
    return {
        'W':0.5,                   # Inertia (Initial Weights)
        'c1':0.8,                  # Cognitive / Personal Best based coefficient (Prioritizes Exploration since it only focuses on the personal's best solution)
        'c2':0.9,                  # Social / Global Best based coefficient (Prioritizes Exploitation since it only focuses on the team's best solution)
        'NumIterations': 1000,     # Number of Iterations to be performed
        'NumParticles': 50,        # Number of Particles to include within the search space
        'targetError': 1e-30,      # Minimum error that must be satisfied before stopping the search
        'plotIntervals': 5,        # Interval in which to plot the search space
        'plotxMin': -5,            # Min x value on the x axis of the plot
        'plotxMax': 5,             # Max x value on the x axis of the plot
        'plotyMin': -5,            # Min y value on the y axis of the plot
        'plotyMax': 5              # Max y value on the y axis of the plot
    }