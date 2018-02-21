ABOUT:

Author: Jakub Wida - 30.01.2018

Contents:
-this catalog contains 3 main parts:
	-Python universal game engine in GameEngine
	-Python game using the engine in DungeonGameEngine

	-Perl level generator in PerlLevelGen.pl

	-Bash highscore management server at HighscoreServer folder, with HighscoreDatabase.sh

Running:
 	>to launch the game: ./GameLauncher.py

	Perl level generator is run automatically by the Python game.

	Bash database is run automatically by the Python game.

Author Comments:
	The game is the most developed part. It is mostly complete, yet leaves room for relatively easy extensions.
	It is written in object fashion, covers event manipulation, keyboard input management, tree of displayed objects etc.

	The generator is a simple piece of software dedicated to a single task: creation of random game levels with random, yet all accesible wall layout, random object distribution, and translation to format understood by python game.

	The highscore database is well, simplistic.
