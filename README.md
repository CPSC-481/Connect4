# Connect4:

Team Members:

Joseph Chau
Daniel Sollis
Dominick Weaver
Sarah Nuno

To run this program, you'll have to download and install PyQt5 library.

After PyQt5 has been installed, you can execute the program once you have downloaded and unzipped the file by inputting:
"python ConnectFour.py"

The player moves first and is the color yellow. Select a column that you would like the token placed, the AI would then play
it's turn, this continues back and forth until a player has 4 of their pieces in a row.

Functional Description of Important Files:

ConnectFour.py:
This is the main file where the games initial settings are declared.

gameOverChecker.py:
This file contains functions that would check if there either player has won.

grid.py:
This file is where our GUI is created.

minimaxFunctions.py:
This file has our minimax algorithm which we implemented for our AI.

naryTree.py:
This file has our state generation.

stateEvaluation:
This file has our heuristic calculations.
