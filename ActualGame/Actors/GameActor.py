from DungeonGameEngine.Game.Actor import Actor
from GameEngine.EventEngine.Event import Event
import curses

class GameActor(Actor):
	def __init__(self,character,coords,color,):
		super().__init__(character,coords,color)
		self.game_component = None

	def on_added_to_game_component(self,Component):
		self.game_component = Component

	def new_event(self,callabl,time_due):
		if self.game_component != None:
			event = Event(callabl)
			event.author = self
			self.game_component.event_engine.add_event(event,time_due)

	def on_removed_from_game_component(self):
		""" this should not be done like this, but im short on time"""
		self.game_component.event_engine.events = [i for i in self.game_component.event_engine.events if i[0].author != self]
		self.game_component = None
