# Connect4:

Team Members:

Joseph Chau

Daniel Sollis

Dominick Weaver

Sarah Nuno

To run this program, you'll have to download and install Qt 5.9.1, as well as the PyQt5 library.

Qt can be found from https://www.qt.io/ while the PyQt library is available through pip

After PyQt5 has been installed, you can execute the program once you have downloaded and unzipped the file by launching the main file 'connnectiFour.py'

The player moves first and is the color yellow, although this can be changed through a global variable in the main file. Select a column that you would like the token placed, the AI will then play
it's turn, this continues back and forth until a player has 4 of their pieces in a row.

Functional Description of Important Files:

ConnectFour.py:
This is the main file where the games initial settings are declared. Most of the GUI setup is done here. The logic for game turns and changing the state of the board is also contained here.

gameOverChecker.py:
This file contains a class that checks if either player has won. This is done by examining each space in the board horizontally, vertically and diagonally. 

grid.py:
This file is where the class created to hold our game board is located. This class contains information about the current game state, setup for the game board's GUI, etc.

minimaxFunctions.py:
This file has our minimax implementation. it works by taking in a list of leaves to a state space. it then propogates those values up using the parent pointer states are given, level by level, until it reaches the final level. The function returns an integer value, that is the column number that it has chosen as its move.

naryTree.py:
This file has our state space class and our state class. Our state space class takes in as parameters a state as the root state, and a ply level int. it automatically generates the state space up to that ply level. our state class contains a parent state, a list of children states, a heuristic value, and information about the game board in this state.

stateEvaluation:
This file has our heuristic evaluation function. Our heuristic works by looking at each possible set of four-in-a-row spaces in a state and assigning each of them a value:
        all blank: 1
        Mixed player: 0
        Single player: 3 to the n, where n is the number of tokens the player has in that four spaces, 
            or infinite if all four are taken. The value is negative if these are the opponents pieces
The values of all of these sets is summed, which gives the heuristic value of that state

