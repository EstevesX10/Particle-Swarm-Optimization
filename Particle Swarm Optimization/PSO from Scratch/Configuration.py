import numpy as np

def loadConfig() -> dict:
    """
    # Description
        -> Simple function that retrives a given configuration to be used inside the PSO Algorithm
    := return: Python Dictionary with the configuration to be used
    """

    # Define variables to calculate and store auxiliar values used in the config dict
    d = 10
    xMin = -100
    xMax = -xMin
    vMin = -0.2*(xMax - xMin)
    vMax = -vMin
    maxIterations = 3000
    populationSize = 10
    w = 0.9 - ((0.9 - 0.4)/maxIterations)*np.linspace(0, maxIterations, maxIterations)

    return {
        'd': d,
        'xMin': xMin,                     # Lower Limit of the Search Space position
        'xMax': xMax,                     # Higher Limit of the Search Space position
        'vMin': vMin,                     # Lower Bound of the Particle's Velocity
        'vMax': vMax,                     # Higher Bound of the Particle's Velocity
        'maxIterations': maxIterations,   # Maximum Number of Iterations
        'populationSize': populationSize, # Population Size

        # The next few parameters can greatly impact the performance of the Algorithm
        'c1': 2,     # Cognitive / Personal Best based coefficient (Prioritizes Exploration since it only focuses on the personal's best solution)
        'r1': ...,   # Random Term to help weight the acceleration c1 (r1 in [0, 2])
        'c2': 2,     # Social / Global Best based coefficient (Prioritizes Exploitation since it only focuses on the team's best solution)
        'r2': ...,   # Random Term to help weight the acceleration c2 (r2 in [0, 2])
        'w': w       # Inertia (Initial Weights)
    }