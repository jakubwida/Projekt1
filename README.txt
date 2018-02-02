ABOUT:

Author: Jakub Wida - 30.01.2018

Contents:
-this catalog contains 3 main parts:
	-Python universal game engine in GameEngine
	-Python game using the engine in DungeonGameEngine

	-Perl level generator in PerlLevelGen.pl

	-Bash highscore sending and viewing script at highscore_viewer.sh
	-Bash highscore management server at HighscoreServer folder

Running:
 	>to launch the game: ./GameLauncher.py
	>to launch the highscore_viewer: ./highscore_viewer
	>to launch the server (nescesary for viewer)-> in folder HighscoreServer: ./highscore_server

	Perl level generator is run automatically by the Python game.

	Python game is separate to the highscore management scripts. After playing, they have to be launched separately - with server first. Server will store highscore information, while viewer retrieves and sends it. Server may be launched on separate machine to the client.

Author Comments:
	The game is the most developed part. It is mostly complete, yet leaves room for relatively easy extensions.
	It is written in object fashion, covers event manipulation, keyboard input management, tree of displayed objects etc.

	The generator is a simple piece of software dedicated to a single task: creation of random game levels with random, yet all accesible wall layout, random object distribution, and translation to format understood by python game.

	The highscore server and viewer are parts of a simple database, dediacted to storing the sending and receiving highscores achieved by the player.
