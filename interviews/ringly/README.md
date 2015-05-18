
Ringly Coding Challenge
=======================

Ground rules
------------

For this coding challenge you may use any programming language you like and you may setup your coding envinronment however you like. You may not discuss the problem or share it with any other people, except the facilitator of the challenge.

For “Level 1” you may use the Internet as a complete resource. Feel free to work on it directly by yourself or google anything you want and read any pages online (excluding chatting directly with people of course). Either approach is fine, but in discussing your result at the end, please share what resources you ended up using.

For “Level 2”, please refrain from using the Internet and only work directly on your computer.

When you complete this challenge, please email back your result and include the code that you wrote (in a Zip or Tar GZip file). Beyond writing code that completes the challenge, some good qualities it should also exhibit are:

*   following the [DRY](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle
*   being easily explainable by you
*   being developed in a way so that another developer could easily pick it up and maintain it

You may finish this very quickly or it may take a while. However, please track your time and at a maximum do not spend more than 3 hours on this challenge. There will be a brief discussion of the solution with the facilitator when you are done.

Please do not share this challenge or your solution with other people (except Ringly, of course!)


The challenge
-------------

This coding challenge involves validating solved Sudoku puzzles.

According to Wikipedia:

> Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 sub-grids that compose the grid (also called "boxes") contains all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a unique solution.

However, as a stone can be cut to have many facets, so can a Sudoku be arranged for other sizes, shapes, and even dimensions. Instead of facing the time-sink of validating puzzles by hand, let’s put technology to work for us by coding up a validator and then putting our mind at ease.


### Level 1 - Cubic Zirconia

The file `sudokus.json` contains various “solved” puzzles. Instead of just the standard 9x9 grid of 3x3 boxes, there are multiple different sizes and shapes, where each row, column, and box still must contain all the numbers from 1 to the size of the collection. Each puzzle has a name, the dimensions of a box for that puzzle, and then a solution as a 2d-array.

Zero or more of the solutions in this JSON file are correct.

Write a script that can read `sudokus.json` and validate each puzzle, outputting the results in any format you like.


## Level 2 - Diamond

The file `sudokus3d.json` follows the same format as its non-3d namesake, except it contains solutions to 3-dimensional Sudokus. You will still be validating grids, but there will now be many inter-locking grids, which all must be correct. For example, a 9x9x9 cube would still have boxes of 3x3 inside each grid and there would be 9+9+9=27 different grids inside the cube that all need to be valid sudokus.

Zero or more of the solutions in this JSON file are correct.

Write a script that can read `sudokus3d.json` and validate each puzzle, outputting the results in any format you like.
