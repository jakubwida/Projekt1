from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene


class Actor(GraphicsObject):
	def __init__(self,character,coords,color):
		super().__init__(coords)
		self.character = character
		self.color = color
		self.game_scene = None

	def set_character(self,character):
		self.character = character

	def set_color(self,color):
		self.color = color

	def on_added_to_game_scene(self,game_scene):
		self.game_scene = game_scene

	def on_removed_from_game_scene(self,game_scene):
		self.game_scene = None

	def tick(self,delta_time,keys,coords):
		self.draw(self.character,self.coords,self.color)
		super().tick(delta_time,keys,coords)
