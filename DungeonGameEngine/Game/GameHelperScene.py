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
		self.keyboard_managet = KeyboardManager()
		self.game_map = GameMap(size)
		self.size = size

		self.actor_list = []

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
		self.event_engine.resolve(delta_time)
		super().tick(delta_time,keys,coords)
