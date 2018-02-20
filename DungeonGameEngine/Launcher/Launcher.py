from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from DungeonGameEngine.Menu.MenuGraphicsObject import MenuGraphicsObject
from DungeonGameEngine.Menu.MenuText import MenuText
from DungeonGameEngine.Menu.MenuButton import MenuButton

from DungeonGameEngine.Game.GameGraphicsObject import GameGraphicsObject
from DungeonGameEngine.Game.GameHelperScene import GameHelperScene

from DungeonGameEngine.Game.GameActor import GameActor
from DungeonGameEngine.Actors.MoverActor import MoverActor

from DungeonGameEngine.Actors.WallActor import WallActor
from DungeonGameEngine.Actors.PlayerActor import PlayerActor
from DungeonGameEngine.Actors.BulletActor import BulletActor
from DungeonGameEngine.Actors.BaddieActor import BaddieActor
from DungeonGameEngine.Actors.PickupActor import PickupActor

from DungeonGameEngine.Actors.Walls.ExitWallActor import ExitWallActor
from DungeonGameEngine.Actors.Pickup.ExitPickupActor import ExitPickupActor
from DungeonGameEngine.Actors.Pickup.MGWeaponPickup import MGWeaponPickup
from DungeonGameEngine.Actors.BaddieActor import BaddieActor
import sys

from DungeonGameEngine.Launcher.LevelReader import LevelReader
from DungeonGameEngine.Launcher.HighscoreCommunicator import HighscoreCommunicator

import datetime
import os


class Launcher:
	def __init__(self):
		self.size = (80,32)

		self.level_reader = LevelReader(self.size)
		self.highscore_commuincator = HighscoreCommunicator(self._button_main_menu,self._button_highscore_summary_menu)

		self.highscore_summary_menu = self.highscore_commuincator.get_name_summary_menu()
		self.highscore_name_input_menu = self.highscore_commuincator.get_name_input_menu()
		self.highscore_viewer = self.highscore_commuincator.get_viewer_menu()

		self.main_menu = self.generate_main_menu()
		self.help_menu = self.generate_help_menu()
		self.options_menu = self.generate_options_menu()
		self.pause_menu = self.generate_pause_menu()
		self.death_screen = self.generate_death_screen()

		self.current_level = None
		self.current_player = None
		self.current_depth = 0
		self.last_depth = 0
		self.get_last_level()
		#---

		config = {"size":self.size}
		self.graphics_engine = GraphicsEngine(config)
		self.graphics_engine.set_root(self.main_menu)


	def launch(self):
		self.graphics_engine.start()


	def _button_newgame(self):
		self.last_depth = 0
		self.reset_level()
		self.graphics_engine.set_root(self.current_level)

	def _button_continue(self):
		self.graphics_engine.set_root(self.current_level)

	def _button_options(self):
		self.graphics_engine.set_root(self.options_menu)

	def _button_help(self):
		self.graphics_engine.set_root(self.help_menu)

	def _button_quit(self):
		sys.exit()

	def _button_main_menu(self):
		self.graphics_engine.set_root(self.main_menu)

	def _button_end_pause(self):
		self.graphics_engine.set_root(self.current_level)

	def _button_highscore_name_input_menu(self):
		self.graphics_engine.set_root(self.highscore_name_input_menu)
		self.highscore_commuincator.set_highscore(self.last_depth)

	def _button_highscore_summary_menu(self):
		self.graphics_engine.set_root(self.highscore_summary_menu)

	def _button_highscore_viewer(self):
		self.graphics_engine.set_root(self.highscore_viewer)

	def _goto_death_screen(self):
		self.reset_level()
		self.graphics_engine.set_root(self.death_screen)

	def _goto_pause_menu(self):
		self.graphics_engine.set_root(self.pause_menu)

	def _on_level_end(self,player):
		self.last_depth = self.current_depth
		self.current_depth+=1
		self.generate_and_get_new_level()
		self.graphics_engine.set_root(self.current_level)

		score = 0
		#if os.path.isfile("current_highscore.txt"):
		#	f = open("current_highscore.txt","r");
		#	lines = f.readlines()
		#	score = int(lines[0].split()[0])
		#if score < self.current_depth:
		#	f = open("current_highscore.txt","w")
		#	f.write(str(self.current_depth)+" ")
		#	now = datetime.datetime.now()
		#	f.write(str(now.year)+":"+str(now.month)+":"+str(now.day)+"\n")

	def generate_main_menu(self):
		t1 = MenuText((3,1),"THE")
		t2 = MenuText((3,2),"DUNGEON")
		t3 = MenuText((3,3),"OF")
		t4 = MenuText((3,4),"CURSES")

		b1 = MenuButton((3,6),"continue",self._button_continue)
		b2 = MenuButton((3,7),"new game",self._button_newgame)
		b3 = MenuButton((3,8),"options",self._button_options)
		b4 = MenuButton((3,9),"help",self._button_help)
		b5 = MenuButton((3,10),"view highscores",self._button_highscore_viewer)
		b6 = MenuButton((3,11),"quit",self._button_quit)
		texts = [t1,t2,t3,t4]
		buttons = [b1,b2,b3,b4,b5,b6]

		mm = MenuGraphicsObject(buttons,texts)

		return mm

	def generate_help_menu(self):
		t1 = MenuText((3,1),"HELP SCREEN")
		t2 = MenuText((3,3),"To navigate in the menus use [arrow keys], and [enter] to select.")
		t3 = MenuText((3,5),"In the game, you controll a \"P\" player.")
		t4 = MenuText((3,6),"In order to progress, shoot all enemies in the room, end reach the \"E\" exit ")
		t5 = MenuText((3,7),"You may use pick-ups to restore health, or get new weapons")
		t6 = MenuText((3,8),"Enemies touching player will decrease health, which at 0 - will cause game over.")
		t7 = MenuText((3,9),"Enemies are underlined.")
		t8 = MenuText((3,10),"[escape] button pauses game, and allows to exit.")
		t9 = MenuText((3,11),"Exiting will allow to continue game later, but with the last room reset.")

		texts = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

		b1 = MenuButton((3,12),"back",self._button_main_menu)

		buttons = [b1]

		hm = MenuGraphicsObject(buttons,texts)
		return hm

	def generate_options_menu(self):
		t1 = MenuText((3,1),"CONTROLS SCREEN")
		t2 = MenuText((3,3),"[arrow keys] move")
		t3 = MenuText((3,4),"[space] shoot")

		texts = [t1,t2,t3]

		b1 = MenuButton((3,12),"back",self._button_main_menu)

		buttons = [b1]

		om = MenuGraphicsObject(buttons,texts)
		return om

	def generate_pause_menu(self):
		t1 = MenuText((3,1),"PAUSE")

		texts = [t1]

		b1 = MenuButton((3,3),"continue",self._button_end_pause)
		b2 = MenuButton((3,4),"main menu",self._button_main_menu)
		b3 = MenuButton((3,5),"quit",self._button_quit)

		buttons = [b1,b2,b3]

		om = MenuGraphicsObject(buttons,texts)
		return om

	def generate_death_screen(self):
		t1 = MenuText((3,1),"YOU HAVE DIED <sadly>")

		texts = [t1]

		b1 = MenuButton((3,3),"main menu",self._button_main_menu)
		b2 = MenuButton((3,4),"quit",self._button_quit)
		b3 = MenuButton((3,5),"upload highscore",self._button_highscore_name_input_menu)

		buttons = [b1,b2,b3]

		om = MenuGraphicsObject(buttons,texts)
		return om


	def get_last_level(self):
		a,b,c = self.level_reader.read_last_level()
		self.current_level = a
		self.current_player = b
		#f = open("log","a")
		#f.write(str(self.current_player.health)+"\n")
		self.current_depth = c
		self._inject_level(self.current_level)

	def reset_level(self):
		self.level_reader.reset_level_save()
		self.get_last_level()

	def generate_and_get_new_level(self):
		self.level_reader.generate_level(self.current_player,self.current_depth)
		self.get_last_level()

	def _inject_level(self,level):
		gs = level.game_scene
		gs.set_on_death(self._goto_death_screen)
		gs.set_on_level_end(self._on_level_end)
		level.set_escape(self._goto_pause_menu)
