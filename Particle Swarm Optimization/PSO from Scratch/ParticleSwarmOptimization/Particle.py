import numpy as np
import random as rnd

class Particle:
    def __init__(self) -> None:
        """
        # Description
            -> Constructor method which allows to create new instances of Particle
        := return: A new instance of Particle
        """
        # Initialize a random position
        x = (-1) ** bool(rnd.getrandbits(1)) * rnd.random() * 1000
        y = (-1) ** bool(rnd.getrandbits(1)) * rnd.random() * 1000
        self.position = np.array([x, y])

        # Initialize the particle's velocity [Static at first]
        self.velocity = np.array([0, 0])

        # Define the personal best position and value
        self.personalBestPosition = self.position
        self.personalBestValue = float('inf')

    def update(self) -> None:
        """
        # Description:
            -> The update method allows the particle to move by adding the velocity to the current position
        := return: None, since we are only updating the particle's position
        """
        # Update current position by adding the veocity
        self.position = self.position + self.velocity