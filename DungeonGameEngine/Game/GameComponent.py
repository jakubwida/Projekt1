from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from GameEngine.EventEngine.EventEngine import EventEngine
from GameEngine.EventEngine.Event import Event

import curses

class GameComponent(GraphicsObject):
	def __init__(self,coords):
		super().__init__(coords)
		self.event_engine = EventEngine()
		self.actor_list = []


	def _on_added_to_game_scene(self,GameScene):
		self.game_scene = GameScene
		self.keyboard_manager = self.game_scene.dungeon_game_engine.keyboard_manager
		self.last_keys_pressed = []

	def add_actor(self,actor):
		self.add_child(actor)
		self.actor_list.append(actor)
		actor.on_added_to_game_scene(self)

	def remove_actor(self,actor):
		self.remove_child(actor)
		self.actor_list.remove(actor)
		actor.on_removed_from_game_scene(self)

	def tick(self,delta_time,keys,coords):
		self.event_engine.resolve(delta_time)
		super().tick(delta_time,keys,coords)
