# This Python Package contains the code used in the developed Particle Swarm Optimization Algorithm

# NOTE: This package contains the implementation of the Particle Swarm Optimization Algorithm provided in the Notebook

# Defining which submodules to import when using from <package> import *
__all__ = ["loadConfig",
           "Particle", "Environment"]

from .Configuration import (loadConfig)
from .Particle import (Particle)
from .Environment import (Environment)