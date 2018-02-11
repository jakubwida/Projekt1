#!/usr/bin/env python3
import getopt
import sys
import traceback
from DungeonGameEngine.Launcher.Launcher import Launcher

f = open("log","w")
f.write("")


try:
	opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
except getopt.GetoptError as err:
	print(err)
	sys.exit(2)

for o, a in opts:
	if o in ("-h", "--help"):
		print("This is the DUNGEON OF CURSES \nto launch it, run this file without passing options. \nThe screen must be at least 80/32 character sized. \nTo navigate in-game menus use arrow keys, and enter to select. \nTo send highscore, use highscore_viewer.sh bash script, if the server is running. \nTo start the highscore server, run highscore_server.sh bash script in HighscoreServer folder. The HighscoreServer folder itself may be set in different locations. \nMore information can be found in -h manuals of said scripts and README file ")
		sys.exit()
	else:
		assert False, "unhandled option"

try:
	l = Launcher()
	l.launch()
except Exception as e:
	print("An error has occured, application has been terminated. \nFile \"log\" contains debugging information")
	print(str(e))
	f = open("log","w")
	f.write("Error:\n")
	f.write(str(e))
	f.write("\n")
	f.write(traceback.format_exc())
