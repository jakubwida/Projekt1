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

import sys



class Launcher:
	def __init__(self):
		self.size = (80,32)

		self.main_menu = self.generate_main_menu()
		self.help_menu = self.generate_help_menu()
		self.options_menu = self.generate_options_menu()
		self.pause_menu = self.generate_pause_menu()
		self.death_screen = self.generate_death_screen()

		#not finished. should read current level rather than generate 0 level
		self.current_level = self.generate_level(0)
		self.level_counter = 0
		#---

		config = {"size":self.size}
		self.graphics_engine = GraphicsEngine(config)
		self.graphics_engine.set_root(self.main_menu)


	def launch(self):
		self.graphics_engine.start()


	def _button_newgame(self):
		self.current_level = self.generate_level(0)
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
		self.graphics_engine.set_root(self.death_screen)

	def _goto_pause_menu(self):
		self.graphics_engine.set_root(self.pause_menu)


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

	#player is unnescesary at 0 level
	def generate_level(self,depth,player=None):
		if depth == 0:
			gs = GameHelperScene(self.size)
			ggo = GameGraphicsObject(gs)

			for i in range(self.size[1]-5):
				gs.add_child(WallActor((0,i)))
				gs.add_child(WallActor((self.size[0]-1,i)))

			#for i in range(1,self.size[0]-6):
			#	gs.add_child(WallActor((i,0)))
			#	gs.add_child(WallActor((i,self.size[0]-1)))

			gs.add_child(PlayerActor((int(self.size[0]/2),int((self.size[1]-5)/2))))
			gs.set_on_death(self._goto_death_screen)
			ggo.set_escape(self._goto_pause_menu)

			return ggo
		else:
			return None
			#NEEDS TO READ LEVEL FROM PERL, OR OTHERWISE COMMUNICATE WITH IT
