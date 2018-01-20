from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from GameEngine.EventEngine.EventEngine import EventEngine
from GameEngine.EventEngine.Event import Event

from DungeonGameEngine.Scene import Scene
#from DungeonGameEngine.Game.GameComponent import GameComponent


from DungeonGameEngine import DungeonGameEngine

class GameScene(Scene):
	def __init__(self,InfoComponent,GameComponent):
		super().__init__()
		self.info_component = InfoComponent
		self.game_component = GameComponent

		self.add_child(self.info_component)
		self.add_child(self.game_component)

		self.on_esc_callable = None

	def on_scene_set(self,DungeonGameEngine):
		super().on_scene_set(DungeonGameEngine)
		self.game_component._on_added_to_game_scene(self)
		self.info_component._on_added_to_game_scene(self)

	def set_on_escape(self,callabl):
		self.on_esc_callable = callabl

	def on_escape(self):
		if self.on_esc_callable != None:
			self.on_esc_callable()

	def tick(self,delta_time,keys,coords):
		if "\x1b" in keys:
			self.on_escape()
		super().tick(delta_time,keys,coords)
