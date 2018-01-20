from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine

from DungeonGameEngine.Menu.MenuScene import MenuScene
from DungeonGameEngine.Menu.MenuObjectText import MenuObjectText
from DungeonGameEngine.Menu.MenuObjectButton import MenuObjectButton

from DungeonGameEngine.Game.GameScene import GameScene
from DungeonGameEngine.Game.GameComponent import GameComponent
from DungeonGameEngine.Game.InfoComponent import InfoComponent
from DungeonGameEngine.Game.Actor import Actor

from GameEngine.Util.GameMap import GameMap

class GameMapComponent(GameComponent):
	def __init__(self):
		super().__init__((0,6))
		self.game_map = GameMap((45,20))

	def add_actor(self,actor):
		self.game_map.set(actor.coords,actor)
		super().add_actor(actor)

	def remove_actor(self,actor):
		self.game_map.set(actor.coords,None)
		super().remove_actor(actor)

	""" assumes that NONE is a clear path"""
	def get_path(self,start_coords,end_coords):
		pass
		#unfinished
