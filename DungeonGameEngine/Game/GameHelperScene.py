from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.AuthorEventEngine.AuthorEventEngine import AuthorEventEngine
from DungeonGameEngine.AuthorEventEngine.AuthorEvent import AuthorEvent

from GameEngine.Util.KeyboardManager import KeyboardManager
from GameEngine.Util.GameMap import GameMap


class GameHelperScene(GraphicsObject):
	def __init__(self,size):
		""" class used in GameGraphicsObject as a child, wih game information. Non universal
		"""
		self.event_engine = AuthorEventEngine()
		self.keyboard_manager = KeyboardManager()
		self.game_map = GameMap(size)
		self.size = size

		self.actor_list = []
		self.last_keys = []

		self.on_level_end = None
		self.on_death = None

		super().__init__([0,5])

	def add_child(self,actor):
		self.actor_list.append(actor)
		self.game_map.set(actor.coords,actor)
		super().add_child(actor)

	def remove_child(self,actor):
		self.actor_list.remove(actor)
		self.game_map.set(actor.coords,None)
		super().remove_child(actor)
		self.event_engine.remove_events_by_author(actor)

	def tick(self,delta_time,keys,coords):
		self.last_keys = self.keyboard_manager.on_keys(keys)
		self.event_engine.resolve(delta_time)
		super().tick(delta_time,keys,coords)

	#callable called on death
	def set_on_death(self,callabl):
		self.on_death = callabl

	#callable called on level ended
	def set_on_level_end(self,callabl):
		self.on_level_end = callabl

	def death(self):
		if self.on_death != None:
			self.on_death()

	def level_end(self):
		if self.on_level_end != None:
			self.on_level_end()
