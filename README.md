<div align="center">
    <h1>Particle Swarm Optimization [Python]</h1>
</div>

<p align="center" width="100%">
    <img src="./Particle Swarm Optimization/Assets/PSO.gif" width="55%" height="55%" />
</p>

<div align="center">
    <a>
        <img src="https://img.shields.io/badge/Made%20with-Python-9ACFC3?style=for-the-badge&logo=Python&logoColor=9ACFC3">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Made%20with-Jupyter-9ACFC3?style=for-the-badge&logo=Jupyter&logoColor=9ACFC3">
    </a>
</div>

<br/>

<div align="center">
    <a href="https://github.com/EstevesX10/Particle-Swarm-Optimization/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/EstevesX10/Particle-Swarm-Optimization?style=flat&logo=gitbook&logoColor=9ACFC3&label=License&color=9ACFC3">
    </a>
    <a href="#">
        <img src="https://img.shields.io/github/repo-size/EstevesX10/Particle-Swarm-Optimization?style=flat&logo=googlecloudstorage&logoColor=9ACFC3&logoSize=auto&label=Repository%20Size&color=9ACFC3">
    </a>
    <a href="#">
        <img src="https://img.shields.io/github/stars/EstevesX10/Particle-Swarm-Optimization?style=flat&logo=adafruit&logoColor=9ACFC3&logoSize=auto&label=Stars&color=9ACFC3">
    </a>
    <a href="https://github.com/EstevesX10/Particle-Swarm-Optimization/blob/main/DEPENDENCIES.md">
        <img src="https://img.shields.io/badge/Dependencies-DEPENDENCIES.md-white?style=flat&logo=anaconda&logoColor=9ACFC3&logoSize=auto&color=9ACFC3"> 
    </a>
</div>

## Project Overview

The objective of this project is to **develop the Particle Swarm Optimization (PSO) algorithm from scratch** in Python. It aims to **implement the core principles** of PSO, including the **initialization of particles**, **velocity updates**, and **position adjustments**, while allowing particles to **converge towards optimal solutions** based on the **balance between exploration and exploitation**.

In addition to developing the PSO algorithm from scratch, I also used the ``pyswarms`` package to **test the algorithm on a few selected objective functions** which allowed to assess the **algorithm's performance**.

## Project Development (Dependencies & Execution)

This project was developed using a `Notebook`. Therefore if you're looking forward to test it out yourself, keep in mind to either use a **[Anaconda Distribution](https://www.anaconda.com/)** or a 3rd party software that helps you inspect and execute it. 

Therefore, for more informations regarding the **Virtual Environment** used in Anaconda, consider checking the [DEPENDENCIES.md](https://github.com/EstevesX10/Particle-Swarm-Optimization/blob/main/DEPENDENCIES.md) file.

## Particle Swarm Optimization

``Particle Swarm Optimization (PSO)`` is an **optimization technique** inspired by the social behavior of birds and fish. It involves **particles (potential solutions)** moving through a search space influenced by both their **own best positions** and the **group's best solution**. 

``Key elements`` include **particle velocity**, **inertia**, and **social and cognitive acceleration factors**, which help **balance exploration and exploitation** of the search space. 

PSO requires **few hyperparameters** which makes it **versatile** and **suitable** for various tasks. ``Adaptive PSO variations`` **adjust parameters dynamically** to **improve optimization performance**.

## Objective Functions

Given the characteristics of the algorithm, I have chosen a **set of objective functions** to **test its performance** on. 

``Objective Functions`` assess each **particle's position** and provide a **fitness value**, allowing the algorithm to **iteratively refine solutions** and approach the **global optimum**.

These functions are designed to **represent a variety of optimization challenges**, providing a comprehensive evaluation of **how well the algorithm adapts to different types of problem spaces**.

<table width="100%">
  <tr>
    <th colspan="3" height="100%">
        <div align="center">
            Objective Functions Selected
        </div>
    </th>
  </tr>
  
  <tr>
    <td width="25%">
        <div align="center">
        <b>Name</b>
        </div>
    </td>
    <td width="25%">
        <div align="center">
        <b>Formula</b>
        </div>
    </td>
    <td width="25%">
        <div align="center">
        <b>3D Graph</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>Sphere</b>
        </div>
    </td>
    <td width="40%">
        <div align="center">
            f(x) = &sum;<sup>d</sup><sub>i=1</sub> x<sub>i</sub><sup>2</sup>
        </div>
    </td>
    <td width="55%">
        <p align="center"><img src="./Particle Swarm Optimization/Assets/SphereFunction.png" height="auto"/>
        </p>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>Rastrigin</b>
        </div>
    </td>
    <td width="40%">
        <div align="center">
            f(x) = 10d + &sum;<sup>d</sup><sub>i=1</sub> [x<sub>i</sub><sup>2</sup> - 10 cos(2&pi;x<sub>i</sub>)]
        </div>
    </td>
    <td width="55%">
        <p align="center"><img src="./Particle Swarm Optimization/Assets/RastriginFunction.png" height="auto"/>
        </p>
    </td>
  </tr>

  <tr>
    <td width="5%">
        <div align="center">
        <b>Rosenbrock</b>
        </div>
    </td>
    <td width="40%">
        <div align="center">
            f(x) = &sum;<sup>d-1</sup><sub>i=1</sub> [100(x<sub>i+1</sub> - x<sub>i</sub><sup>2</sup>)<sup>2</sup> + (x<sub>i</sub> - 1)<sup>2</sup>]
        </div>
    </td>
    <td width="55%">
        <p align="center"><img src="./Particle Swarm Optimization/Assets/RosenbrockFunction.png" height="auto"/>
        </p>
    </td>
  </tr>

</table>

## Project Results

Here are the results obtained by using the ``pyswarms`` package to **minimize** the previously selected **objective functions**.

<table width="100%">
  <tr>
    <th colspan="4" height="100%">
        <div align="center">
            PSO Results
        </div>
    </th>
  </tr>

  <tr>
    <td width="10%">
        <div align="center">
        <b>Objective Function</b>
        </div>
    </td>
    <td width="30%">
        <div align="center">
        <b>Cost History</b>
        </div>
    </td>
    <td width="20%">
        <div align="center">
        <b>2D Particle Search</b>
        </div>
    </td>
    <td width="30%">
        <div align="center">
        <b>3D Particle Search</b>
        </div>
    </td>
  </tr>

  <tr>
    <td width="10%">
        <div align="center">
        <b>Sphere</b>
        </div>
    </td>
    <td width="10%">
        <p align="center"><img src="./Particle Swarm Optimization/PSO with Pyswarms/Cost History/SphereCostHistory.png"/>
        </p>
    </td>
    <td width="10%">
        <p align="center"><img src="./Particle Swarm Optimization/PSO with Pyswarms/Particle Searches/2D_SphereParticlesSearch.gif" height="auto"/>
        </p>
    </td>
    <td width="50%">
        <p align="center"><img src="./Particle Swarm Optimization/PSO with Pyswarms/Particle Searches/3D_SphereParticlesSearch.gif" height="auto"/>
        </p>
    </td>
  </tr>

  <tr>
    <td width="10%">
        <div align="center">
        <b>Ratrigin</b>
        </div>
    </td>
    <td width="30%">
        <p align="center"><img src="./Particle Swarm Optimization/PSO with Pyswarms/Cost History/RastriginCostHistory.png"/>
        </p>
    </td>
    <td width="30%">
        <p align="center"><img src=".//Particle Swarm Optimization/PSO with Pyswarms/Particle Searches/2D_RastriginParticlesSearch.gif" height="auto"/>
        </p>
    </td>
    <td width="30%">
        <p align="center"><img src=".//Particle Swarm Optimization/PSO with Pyswarms/Particle Searches/3D_RastriginParticlesSearch.gif" height="auto"/>
        </p>
    </td>
  </tr>

  <tr>
    <td width="10%">
        <div align="center">
        <b>Rosenbrock</b>
        </div>
    </td>
    <td width="30%">
        <p align="center"><img src="./Particle Swarm Optimization/PSO with Pyswarms/Cost History/RosenbrockCostHistory.png"/>
        </p>
    </td>
    <td width="30%">
        <p align="center"><img src="./Particle Swarm Optimization/PSO with Pyswarms/Particle Searches/2D_RosenbrockParticlesSearch.gif" height="auto"/>
        </p>
    </td>
    <td width="30%">
        <p align="center"><img src="./Particle Swarm Optimization/PSO with Pyswarms/Particle Searches/3D_RosenbrockParticlesSearch.gif" height="auto"/>
        </p>
    </td>
  </tr>
</table>

These results demonstrate how effectively the **algorithm minimizes these functions**, highlighting its **versatility** and **performance** across diverse problem landscapes.

<div align="right">
<sub>

<!-- <sup></sup> -->
`README.md by Gonçalo Esteves`
</sub>
</div>