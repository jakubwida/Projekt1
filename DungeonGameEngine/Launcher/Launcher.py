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


class Launcher:
	def __init__(self):
		self.size = (80,32)

		self.level_reader = LevelReader()


		self.main_menu = self.generate_main_menu()
		self.help_menu = self.generate_help_menu()
		self.options_menu = self.generate_options_menu()
		self.pause_menu = self.generate_pause_menu()
		self.death_screen = self.generate_death_screen()

		a,b,c = self.read_last_level()
		self.current_level = a
		self.current_player = b
		self.level_counter = c
		#---

		config = {"size":self.size}
		self.graphics_engine = GraphicsEngine(config)
		self.graphics_engine.set_root(self.main_menu)


	def launch(self):
		self.graphics_engine.start()


	def _button_newgame(self):
		self.reset_game()
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

	def _goto_death_screen(self):
		self.reset_game()
		self.graphics_engine.set_root(self.death_screen)

	def _goto_pause_menu(self):
		self.graphics_engine.set_root(self.pause_menu)

	def reset_game(self):
		self.current_level = self.generate_level(0)
		self.current_player = PlayerActor([0,0])
		self.level_counter = 0
		self.level_reader.reset_level_save()

	#TEMPORARY
	def _on_level_end(self,player):
		self.current_player = player
		self.level_counter+=1
		self.current_level = self.generate_level(self.level_counter)
		self.graphics_engine.set_root(self.current_level)

	def generate_main_menu(self):
		t1 = MenuText((3,1),"THE")
		t2 = MenuText((3,2),"DUNGEON")
		t3 = MenuText((3,3),"OF")
		t4 = MenuText((3,4),"CURSES")

		b1 = MenuButton((3,6),"continue",self._button_continue)
		b2 = MenuButton((3,7),"new game",self._button_newgame)
		b3 = MenuButton((3,8),"options",self._button_options)
		b4 = MenuButton((3,9),"help",self._button_help)
		b5 = MenuButton((3,10),"quit",self._button_quit)

		texts = [t1,t2,t3,t4]
		buttons = [b1,b2,b3,b4,b5]

		mm = MenuGraphicsObject(buttons,texts)

		return mm

	def generate_help_menu(self):
		t1 = MenuText((3,1),"HELP SCREEN")
		t2 = MenuText((3,3),"To navigate in menu's use [arrow keys], and [enter] to select.")
		t3 = MenuText((3,5),"In the game, you controll a \"P\" player.")
		t4 = MenuText((3,6),"In order to progress, shot all enemies in the room, end reach the \"E\" exit ")
		t5 = MenuText((3,7),"You may use pick-ups to restore health, or get new weapons")
		t6 = MenuText((3,8),"Enemies touching player will decrease health. No health ends game.")
		t7 = MenuText((3,9),"Enemies are underlined. Pick-ups are blinking")
		t8 = MenuText((3,10),"[escape] button pauses game, and possibly exit.")
		t9 = MenuText((3,11),"Exiting will allow to continue game later, but with the last room reset.")

		texts = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

		b1 = MenuButton((3,12),"back",self._button_main_menu)

		buttons = [b1]

		hm = MenuGraphicsObject(buttons,texts)
		return hm

	def generate_options_menu(self):
		t1 = MenuText((3,1),"OPTIONS SCREEN - NON MUTABLE PLACEHOLDER")
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

		buttons = [b1,b2]

		om = MenuGraphicsObject(buttons,texts)
		return om


	def generate_level(self,depth):

		ggo = self.level_reader.generate_level(self.size,depth,self.current_player)

		"""
		gs = ggo.game_scene

		gs.set_on_death(self._goto_death_screen)
		gs.set_on_level_end(self._on_level_end)

		ggo.set_escape(self._goto_pause_menu)
		"""
		self._inject_level(ggo)

		return ggo

	def read_last_level(self):
		level,player,depth = self.level_reader.read_last_level()
		self._inject_level(level)
		return level,player,depth

	def _inject_level(self,level):
		gs = level.game_scene
		gs.set_on_death(self._goto_death_screen)
		gs.set_on_level_end(self._on_level_end)
		level.set_escape(self._goto_pause_menu)
