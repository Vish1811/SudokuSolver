# SudokuSolver
This repository contains an interesting project called Sudoko Solver
If done properly,it should solve the given Sudoku problem effeciently.

# AIM
Create a python Program that:-
## Basic Module
1. Solve the Sudoku using the BACKTRACKING Approach (Solution in the Terminal)
## Intermediate Module
2. Solve the Sudoku using the BACKTRACKING Approach (Solution using GUI)
## Advanced Module
3. Extracting the Sudoku Problem from a image of the Newspaper using Image Processing.(Machine Learning)
4. Solve the problem Extracted form the image and show the result in the form of GUI.

# TASK LIST

- [ ] Work out complete structure of project. Enlist all libraries needed, have a basic idea of thier working.
- [ ] Write basic python program to execute this
- [ ] Write C++ program to solve   
- [ ] Create GUI, integrate it
- [ ] Deploy in form of website
- [ ] Study to implement advance ML features(point 3,4)

# Technlogy used
1. Python
2. pygame
2. GUI
3. Machine Learning (KNN)
4. Image Processing

# Problem Statement

Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9.

## Algorithms to Solve
1. ### Naive Algorithm
The Naive Algorithm is to generate all possible configurations of numbers from 1 to 9 to fill the empty cells. Try every configuration one by one until the correct configuration is found.

Time Complexity O(9^81)

2. ### Using Backtraking

1. Find row, col of an unassigned cell
2. If there is none, return true
3. For digits from 1 to 9
    a) If there is no conflict for digit at row, col
        assign digit to row, col and recursively try fill in rest of grid
    b) If recursion successful, return true
    c) Else, remove digit and try another
4. If all digits have been tried and nothing worked, return false
