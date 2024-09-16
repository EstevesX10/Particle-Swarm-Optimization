import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from .Particle import (Particle)

class Environment():
    def __init__(self, target:int, config:dict) -> None:
        """
        # Description
            -> Constructor method which allows to create new instances of Space
        := param: target - Fitness Score to reach (The place where all the particles must converge to has the higher score)
        := param: config - Configuration to be used during the particles search
        := return: A new instance of Space
        """
        # Store all the given parameters
        self.target = target
        self.config = config

        # Create a list to store all the Particles
        self.particles = [Particle() for _ in range(self.config['NumParticles'])]

        # Define the initial global best position and value
        self.globalBestValue = float('inf')
        self.globalBestPosition = np.array([rnd.random() * 50, rnd.random() * 50])

    # In this implementation the objective function is give by: f = x^2 + y^2 + 1
    def fitness(self, particle:Particle) -> int:
        """
        # Description
            -> The fitness method is responsible for performing the fitness score evaluation according to the objective function
        := param: particle - Instance of the previously implemented Particle class
        := return: Fitness score of the given particle
        """
        x = particle.position[0]
        y = particle.position[1]
        f = x**2 + y**2 + 1
        return f

    def setPersonalBest(self) -> None:
        """
        # Description
            -> This method is responsible for Updating the particles personal best position and value if any was found
        := return: None, since it is updating the particles attributes
        """
        # Loop over the Particles
        for particle in self.particles:
            # Calculate the fitness score of the current particle
            fitnessScore = self.fitness(particle)

            # Found a particle that lead to a better result (lead to a better fitnessScore) 
            if (particle.personalBestValue > fitnessScore):
                # Update personal best value and position
                particle.personalBestValue = fitnessScore
                particle.personalBestPosition = particle.position

    def setGlobalBest(self) -> None:
        """
        # Description:
            -> The setGlobalBest method updates the global best value and position if any was found
        := return: None, since it is only updating values
        """
        # Loop over the particles
        for particle in self.particles:
            # Calculate current particle fitness score
            bestFitnessScore = self.fitness(particle)

            # Check if the current fitness score is better than the global one 
            if (self.globalBestValue > bestFitnessScore):
                # Update the Global best variables
                self.globalBestValue = bestFitnessScore
                self.globalBestPosition = particle.position

    def updateParticles(self) -> None:
        """
        # Description
            -> This method updates the particle's position according to a new calculated velocity
        := return: None, since it is only updating the particles position and velocity
        """
        # Loop over the Particles
        for particle in self.particles:
            # Calculate the inertia according to the particle's velocity
            inertia = self.config['W'] * particle.velocity

            # Calculate self and swarm confidences
            selfConfidence = self.config['c1'] * rnd.random() * (particle.personalBestPosition - particle.position)
            swarmConfidence = self.config['c2'] * rnd.random() * (self.globalBestPosition - particle.position)

            # Get a new velocity
            newVelocity = inertia + selfConfidence + swarmConfidence

            # Update the particle's velocity and position
            particle.velocity = newVelocity
            particle.update()

    def showParticles(self, iteration:int) -> None:
        """
        # Description
            -> The showParticles method creates a plot to visualize the particles position within a given iteration
        := return: None, since it is only plotting the particles data
        """
        # Print current iteration and the corresponding global values
        print(f"\n{iteration} iteration(s)")
        print(f"[Current Best Position] : {self.globalBestPosition}")
        print(f"[Current Best Value / Fitness Score] : {self.globalBestValue}")

        # Loop over the particles and add their data into the plot
        for particle in self.particles:
            plt.plot(particle.position[0], particle.position[1], 'ro')
        plt.plot(self.globalBestPosition[0], self.globalBestPosition[1], 'bo')
        
        # Set the limits for x and y axes to keep the scale constant
        plt.xlim(self.config['plotxMin'], self.config['plotxMax'])
        plt.ylim(self.config['plotyMin'], self.config['plotyMax'])

        # Show the plot
        plt.show()

    def performSearch(self) -> None:
        """
        # Description
            -> This method is responsible for performing search with the particles towards the goal
        := param: NumIterations - Number of iterations to be performed
        := return: None, due to the fact that we are merely performing search with the particles towards a common goal
        """
        # Perform <NumInterations> iterations
        for iteration in range(self.config['NumIterations']):
            # Set particles best and global best 
            self.setPersonalBest()
            self.setGlobalBest()

            # Plot the current iteration
            if ((iteration + 1) % self.config['plotIntervals'] == 0):
                self.showParticles(iteration)

            # Check if the current error is small enough and therefore stop the iterations
            if (abs(self.globalBestValue - self.target) <= self.config['targetError']):
                print(f"[Global Best Position] : {self.globalBestPosition} -> Found in {iteration + 1} iteration(s)")
                return

            # Update particles
            self.updateParticles()

        # Print the best solution
        print(f"[Global Best Position] : {self.globalBestPosition} -> Found in {self.config['NumIterations'] + 1} iteration(s)")