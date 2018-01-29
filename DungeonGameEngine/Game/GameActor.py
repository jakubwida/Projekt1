from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject
from DungeonGameEngine.AuthorEventEngine.AuthorEvent import AuthorEvent



class GameActor(GraphicsObject):
	def __init__(self,coords,character="A",color=None):
		self.character = character
		self.color = color
		super().__init__(coords)

		#dict used in collisions. key = object class, value = function called when colliding with said object
		self.collision_dict = None

	def new_event(self,callabl,time_due):
		""" creates a new event whitch it is athor of. upon die() events are removed. event manager is in GameHelperScene.
		callabl -> called when event is done
		time_due -> time till event runs
		"""
		ai = AuthorEvent(callabl,self)
		if self.parent !=None:
			self.parent.event_engine.add_event(ai,time_due)

	def spawn_actor(self,new_actor):
		""" safely places a new actor (new_actor) in GameHelperScene"""
		if self.parent != None:
			if self.parent.game_map.get(new_actor.coords) == None:
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
		calls one of collide_player etc. depending on what type is the collidor
		collidor-> target object"""

		if self.collision_dict == None:
			from DungeonGameEngine.Actors.WallActor import WallActor
			from DungeonGameEngine.Actors.PlayerActor import PlayerActor
			from DungeonGameEngine.Actors.BulletActor import BulletActor
			from DungeonGameEngine.Actors.BaddieActor import BaddieActor
			from DungeonGameEngine.Actors.PickupActor import PickupActor

			self.collision_dict = {}
			self.collision_dict[WallActor] = self.collide_wall
			self.collision_dict[PlayerActor] =self.collide_player
			self.collision_dict[BulletActor] = self.collide_bullet
			self.collision_dict[BaddieActor] =self.collide_baddie
			self.collision_dict[PickupActor] =self.collide_pickup

		for k,v in self.collision_dict.items():
			if isinstance(collidor,k):
				v(collidor)

	def die(self):
		""" removes itself safely from the GameHelperScene"""
		if self.parent != None:
			self.parent.remove_child(self)

	def tick(self,delta_time,keys,coords):
		""" draws self.character at relative 0,0 <it's position>, and uses self.color to color itself."""
		self.draw(self.character,[0,0],self.color)
		super().tick(delta_time,keys,coords)


	def collide_wall(self,collidor):
		""" called in collide if collidor is wall"""
		pass

	def collide_player(self,collidor):
		""" called in collide if collidor is player"""
		pass

	def collide_bullet(self,collidor):
		""" called in collide if collidor is bullet"""
		pass

	def collide_baddie(self,collidor):
		""" called in collide if collidor is baddie"""
		pass

	def collide_pickup(self,collidor):
		""" called in collide if collidor is pickup"""
		pass
