# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:47:29 2019

@author: michael
"""


import numpy as np
import math
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import time


grid = np.array([])

vals = [0,1,2,3]

def randomGrid(N): 

	"""returns a grid of NxN random values"""
	return np.random.choice(vals, N*N).reshape(N, N) 

def stackedGrid(N, m):
    
    """returns an NxN grid of zeros, with m in the middle square"""
    grid = np.zeros((N,N), dtype=int)
    center = math.floor(N/2)
    grid[center,center] = m
    return grid


def updateGrid(grid):

    hist = [grid]
    while np.max(grid) > 3:              
        newgrid = grid.copy()       
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i,j] > 3:
                    newgrid[i,j] -= 4
                    if i > 0:
                        newgrid[i-1,j] += 1
                    if i < grid.shape[0]-1:
                        newgrid[i+1,j] += 1
                    if j < grid.shape[1]-1:
                        newgrid[i,j+1] += 1
                    if j > 0:
                        newgrid[i,j-1] += 1

        grid = newgrid.copy()
    return grid, hist
    