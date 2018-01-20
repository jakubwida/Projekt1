from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine


class Scene(GraphicsObject):
	""" a simeple GraphicsObject extension, that requires DungeonGameEngine as a parameter. Used for root-child level contatiners. passed to DungeonGameEngine via set_scene()"""
	def __init__(self):
		super().__init__([0,0])
		self.dungeon_game_engine = None


	def on_scene_set(self,DungeonGameEngine):
		""" called when set to DungeonGameEngine"""
		self.dungeon_game_engine = DungeonGameEngine

	def on_scene_unset(self):
		""" called when un-set from DungeonGameEngine"""
		self.dungeon_game_engine = None
