import numpy as np
import matplotlib.pyplot as plt
from .Configuration import (loadConfig)

def limitVelocity(velocity:np.ndarray, config:dict) -> np.ndarray:
    """
    # Description:
        -> This function helps manage and control the limits of the particles velocity
    
    := param: velocity - Numpy array with the current velocities of all particles
    := param: config - Configuration dictionary used in the Algorithm
    := return: A new numpy array with the updated values of velocity
    """

    # Loop over the velocity array
    for particleIdx in range(len(velocity)):
        # Check if the current particle's velocity surpassed the maximum value defined
        if (velocity[particleIdx] > config['vMax']):
            velocity[particleIdx] = config['vMax']
        # Check if the current particle's velocity is lower than the minimum value defined
        elif (velocity[particleIdx] < config['vMin']):
            velocity[particleIdx] = config['vMin']
        
    # Return the updated version of the array
    return velocity

def limitPosition(position:np.ndarray, config:dict) -> np.ndarray:
    """
    # Description:
        -> This function helps manage and control the limits of the particles position
    
    := param: position - Numpy array with the current position of all particles
    := param: config - Configuration dictionary used in the Algorithm
    := return: A new numpy array with the updated values of the positions
    """

    # Loop over the position array
    for particleIdx in range(len(position)):
        # Check if the current particle's position surpassed the maximum value defined
        if (position[particleIdx] > config['xMax']):
            position[particleIdx] = config['xMax']
        # Check if the current particle's position is lower than the minimum value defined
        elif (position[particleIdx] < config['xMin']):
            position[particleIdx] = config['xMin']
        
    # Return the updated version of the array
    return position

class Particle():
    def __init__(self, config:dict) -> None:
        """
        # Description:
            -> Constructor method which allows the creation of instances of the Object Particle
        
        := param: config - Python Dictionary with the configuration used inside the Particle Swarm Optimization Algorithm
        := return: A new instance of the Object Particle
        """
        # Store the config
        self.config = config

        # Define the initial position of the Particle (It is randomly generated within [xMin, 50])
        self.position = np.random.uniform(config['xMin'], 50, [config['populationSize'], config['d']])

        # Define the Initial velocity of the Particle (It is randomly generated within [vMin, 50])
        self.velocity = np.random.uniform(config['vMin'], config['vMax'], [config['populationSize'], config['d']])
    
        # Define the initial fitness value aka cost
        self.cost = np.zeros(config['populationSize'])

        # Update the cost by applying the Funtion to the current position to get its fitness value
        self.cost[:] = self.config['function']((self.position[:]))

        # Define both Personal best position and personal best cost
        self.personalBestPosition = np.copy(self.position)
        self.personalBestCost = np.copy(self.cost)

        # Define a index attribute to store the idx of the position which has the minimum personal best cost (Used to define the global best)
        self.index = np.argmin(self.personalBestCost)

        # Define both the Global Best position and cost
        self.globalBestPosition = self.personalBestPosition[self.index]
        self.globalBestCost = self.personalBestCost[self.index]

        # Create a array to store all the data from each iteration
        self.bestCostPerIteration = np.zeros(config['maxIterations'])

    def evaluate(self) -> None:
        """
        # Description:
            -> This method is responsible for evaluating the particles position and velocity attending to minimize the personal and global costs towards the solution
        := return: None, since it only processes the data and stores it inside the self.bestCostPerIteration attribute
        """
        for iterationIdx in range(self.config['maxIterations']):
            for particleIdx in range(self.config['populationSize']):
                # Update the Velocity
                self.velocity[particleIdx] = ((self.config['w'][iterationIdx] * self.velocity[particleIdx]) +
                                              (self.config['c1'] * np.random.rand(self.config['d']) * (self.personalBestPosition[particleIdx] - self.position[particleIdx])) + 
                                              (self.config['c2'] * np.random.rand(self.config['d']) * (self.globalBestPosition[particleIdx] - self.position[particleIdx]))
                                              )
                
                # Limit the Velocity values to make sure they do not breach the previously defined boundaries
                self.velocity[particleIdx] = limitVelocity(self.velocity[particleIdx], self.config)

                # Update the Position
                self.position[particleIdx] += self.velocity[particleIdx]

                # Limit the Position values to make sure they do not breach the previously defined boundaries
                self.position[particleIdx] = limitPosition(self.position[particleIdx], self.config)

                # Update current particle's cost
                self.cost[particleIdx] = self.config['function']((self.position[particleIdx]))

                # In this case we want to minimize the cost
                # Therefore we check if the current cost is better than the personal best one
                if (self.cost[particleIdx] < self.personalBestCost[particleIdx]):
                    # Update the personal best position and cost to the discovered values
                    self.personalBestPosition[particleIdx] = self.position[particleIdx]
                    self.personalBestCost[particleIdx] = self.cost[particleIdx]

                    # Check if the personal best cost is better (eg, lower) than the global ones
                    if self.personalBestCost[particleIdx] < self.globalBestCost:
                        # Update the global best 
                        self.globalBestPosition = self.personalBestPosition[particleIdx]
                        self.globalBestCost = self.personalBestCost[particleIdx]
                
                # Store the new processed data
                self.bestCostPerIteration[iterationIdx] = self.globalBestCost
        
    def plotResults(self) -> None:
        """
        # Description:
            -> The plotResults method is responsible for plotting the previously collected data
        := return: None, since it only focuses on showing the processed data
        """
        plt.semilogy(self.bestCostPerIteration)
        print(f"Best Fitness Value = ", self.globalBestCost)
        plt.show()

def Optimization():
    # Load the config 
    config = loadConfig()
            
    # Crate a new instance of the Particle
    particle = Particle(config)

    # Perform Evaluation
    particle.evaluate()

    # Plot the Results
    particle.plotResults()