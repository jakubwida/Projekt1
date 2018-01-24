from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject
from DungeonGameEngine.AuthorEventEngine.AuthorEvent import AuthorEvent

class GameActor(GraphicsObject):
	def __init__(self,coords,character="A",color=None):
		self.character = character
		self.color = color
		super().__init__(coords)

	def new_event(self,callabl,time_due):
		""" creates a new event whitch it is athor of. upon die() events are removed. event manager is in GameHelperScene.
		callabl -> called when event is done
		time_due -> time till event runs
		"""
		ai = AuthorEvent(callabl,self)
		self.parent.event_engine.add_event(ai,time_due)

	def spawn_actor(self,new_actor):
		""" safely places a new actor (new_actor) in GameHelperScene"""
		self.parent.add_child(new_actor)

	def reposition(self,new_position):
		""" moves self within GameHelperScene. If a target is not None, calls collide(target)
		new_position -> where to is it moving
		"""

		target = self.parent.game_map.get(new_position)
		if not target == None:
			self.collide(target)
		else:
			self.parent.game_map.set(self.coords,None)
			self.parent.game_map.set(new_position,self)
			self.coords = new_position


	def collide(self,collidor):
		""" called when object is reposition() -ed to a position with not None occupying it
		collidor-> target object"""
		pass

	def die(self):
		""" removes itself safely from the GameHelperScene"""
		self.parent.remove_child(self)

	def tick(self,delta_time,keys,coords):
		""" draws self.character at relative 0,0 <it's position>, and uses self.color to color itself."""
		self.draw(self.character,[0,0],self.color)
		super().tick(delta_time,keys,coords)
