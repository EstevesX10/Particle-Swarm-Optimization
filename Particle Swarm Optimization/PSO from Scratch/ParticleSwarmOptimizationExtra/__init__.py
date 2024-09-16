# This Python Package contains the code used in the developed Particle Swarm Optimization Algorithm

# NOTE: This package contains a different implementation of the Particle Swarm Optimization Algorithm than the one provided in the Notebook

# Defining which submodules to import when using from <package> import *
__all__ = ["Particle", "Optimization",
           "loadConfig",
           "sphereFunction", "rosenbrockFunction"]

from .ParticleSwarmOptimization import (Particle, Optimization)
from .Configuration import (loadConfig)
from .Functions import (sphereFunction, rosenbrockFunction)