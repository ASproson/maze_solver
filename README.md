# Maze Solver

This project implements an DFS algorithm to solve randomly generated mazes in Python

## Technical Walkthrough

### graphics.py

Here we establish the `Window` class which is our browser instance. We then draw to that `Canvas` using various `Lines` that are drawn from `Point` to `Point`

### cell.py

This file then makse use of the `Line` and `Point` methods to both draw all the cells in the grid and the 'solving' line. Note the use of `wall_color(self.has_right_wall)`, this is what we use to 'color' a line to determine whether or not it has a wall. To be more specific a wall is _always_ drawn regardless, but by changing its color to white it provides a better visualization

### maze.py

This creates the grid and generates the number of cells required based on the specified grid height and width. The `animate()` method is what provides the 'drawing' animation by calling `redraw()`, which allows us to visualize both the initial grid and the grid updates as the algorithm solves the maze

The _break_ and _solve_ methods are the core of the DFS algorithm, and calculate which directions are available for us to move in (up/down/left/right), and which walls to 'break down' as a result (re-color is a more description based on `cell.py`)

The rows are specified as `i`, with columns denoting `j`. To move up we have to _subtract_ from `i` (rows) so that we select the row above, to move left we have to subtract of `j` (cols). The main technical challenge here was ensuring this calculation always remained within the index bounds of list

### main.py

Here we pass the core parameters such as number of rows/columns, and the overall height of the canvas we would like to draw to. Additionally, there is a `seed` that we can pass that fixes the randomization to a specific pattern, which I predominately used for testing purposes

# Demonstration
![Animation](https://github.com/ASproson/maze_solver/assets/77736272/19a8a712-554d-439f-9e1d-00ac795d10e4)

![Animation2](https://github.com/ASproson/maze_solver/assets/77736272/a9c9b860-4f2b-49b7-a757-74d7e0738057)
