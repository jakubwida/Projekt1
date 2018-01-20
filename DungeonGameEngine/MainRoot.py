from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine import DungeonGameEngine

class MainRoot(GraphicsObject):
	def __init__(self,DungeonGameEngine):
		super().__init__([0,0])
		self.dungeon_game_engine = DungeonGameEngine
		self.scene = None

	def tick(self,delta_time,keys,coords):
		super().tick(delta_time,keys,coords)
		self.dungeon_game_engine._pass_keys(keys)

	def set_scene(self,new_scene):
		if self.scene != None:
			self.remove_child(self.scene)
			self.scene.on_scene_unset()

		self.scene = new_scene
		self.add_child(self.scene)
		self.scene.on_scene_set(self.dungeon_game_engine)
