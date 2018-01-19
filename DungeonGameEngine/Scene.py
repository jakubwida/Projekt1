from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine

class Scene(GraphicsObject):
	def __init__(self):
		super().__init__([0,0])
		self.dungeon_game_engine = None

	def on_scene_set(self,DungeonGameEngine):
		self.dungeon_game_engine = DungeonGameEngine

	def on_scene_unset(self):
		self.dungeon_game_engine = None
