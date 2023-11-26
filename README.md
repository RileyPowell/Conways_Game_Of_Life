# Conways_Game_Of_Life
A simulator of John Conway's Game of Life written in python using Numpy.

rules: 
* each cell can be alive (1) or dead (0).
* if a cell is alive and it has two or three touching cells which are alive, it will stay alive.
* if a cell is dead and it has three touhing cells which are alive, it will become alive.
* if a cell is alive and has four or more living cells touching it it will die.
* if a cell is alive and has less than two living cells touching it it will die.

## Images generated from the scripts of the game board.

| ![Conway GOL initial state](https://github.com/RileyPowell/Conways_Game_Of_Life/assets/151593109/60e0e44e-0a25-4809-b59b-4bfdca600ae4) |
|:--:| 
| *Conway Game of Life initial board state* |

| ![Conway GOL after 3 steps](https://github.com/RileyPowell/Conways_Game_Of_Life/assets/151593109/3f4b9f6c-e7d4-4ad5-9bce-32978302c301) |
|:--:| 
| *Conway Game of Life after 3 steps* |
