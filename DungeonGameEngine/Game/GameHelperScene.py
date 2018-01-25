from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.AuthorEventEngine.AuthorEventEngine import AuthorEventEngine
from DungeonGameEngine.AuthorEventEngine.AuthorEvent import AuthorEvent

from GameEngine.Util.KeyboardManager import KeyboardManager
from GameEngine.Util.GameMap import GameMap

from DungeonGameEngine.Actors.Pickup.ExitPickupActor import ExitPickupActor
from DungeonGameEngine.Actors.Walls.ExitWallActor import ExitWallActor
from DungeonGameEngine.Actors.BaddieActor import BaddieActor
from DungeonGameEngine.Actors.PlayerActor import PlayerActor

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

		self.baddie_counter = 0

		super().__init__([0,5])

	def add_child(self,actor):
		self.actor_list.append(actor)
		self.game_map.set(actor.coords,actor)
		super().add_child(actor)
		if isinstance(actor,BaddieActor):
			self.baddie_added()

	def remove_child(self,actor):
		self.actor_list.remove(actor)
		self.game_map.set(actor.coords,None)
		super().remove_child(actor)
		self.event_engine.remove_events_by_author(actor)
		if isinstance(actor,BaddieActor):
			self.baddie_died()

	def tick(self,delta_time,keys,coords):
		self.last_keys = self.keyboard_manager.on_keys(keys)
		self.event_engine.resolve(delta_time)
		super().tick(delta_time,keys,coords)

	def baddie_added(self):
		self.baddie_counter +=1

	def baddie_died(self):
		self.baddie_counter -=1
		if self.baddie_counter <= 0:
			for i in self.children:
				if isinstance(i,ExitWallActor):
					coords = list(i.coords)
					i.die()
					self.add_child(ExitPickupActor(coords))

	#callable called on death
	def set_on_death(self,callabl):
		self.on_death = callabl

	#callable called on level ended
	def set_on_level_end(self,callabl):
		self.on_level_end = callabl

	def death(self):
		if self.on_death != None:
			self.on_death()

	def level_end(self,player):
		if self.on_level_end != None:
			self.on_level_end(player)
