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

def rosenbrockFunction(x:np.ndarray) -> float:
    """
    # Description:
        -> Rosenbrock Function used inside the Research Paper [Summation of (x_i)^2, for i in [1, dim(x)]]
    
    := param x: Numpy array with an nth-dimensional shape
    := return: Approximation of the function given a input array
    """
    total = 0.0
    for idx in range(x.size - 1):
        total += (100 * (x[idx]**2 - x[idx+  1])**2 + (x[idx] - 1)**2)
    return total