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
		self.game_scene = None


	def _on_added_to_game_scene(self,GameScene):
		self.game_scene = GameScene
		self.keyboard_manager = self.game_scene.dungeon_game_engine.keyboard_manager
		self.last_keys_pressed = []
		for i in self.children:
			i.on_added_to_game_scene(self.game_scene)

	def add_actor(self,actor):
		self.add_child(actor)
		self.actor_list.append(actor)
		if self.game_scene != None:
			actor.on_added_to_game_scene(self.game_scene)
		actor.on_added_to_game_component(self)

	def remove_actor(self,actor):
		self.remove_child(actor)
		self.actor_list.remove(actor)
		actor.on_removed_from_game_scene()
		actor.on_removed_from_game_component()

	def tick(self,delta_time,keys,coords):
		if(self.game_scene != None) and (self.game_scene.dungeon_game_engine != None):
			self.last_keys_pressed = self.game_scene.dungeon_game_engine.last_keys_pressed
		#if len(self.last_keys_pressed) > 0:
		#	f = open("log",'a')
		#	f.write("component:"+str(self.last_keys_pressed))
		self.event_engine.resolve(delta_time)
		super().tick(delta_time,keys,coords)
