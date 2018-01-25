from DungeonGameEngine.Actors.BaddieActor import BaddieActor
from DungeonGameEngine.Actors.PlayerActor import PlayerActor
import random
import math

class BulletBaddieActor(BaddieActor):
	def __init__(self,coords,direction):
		super().__init__(coords,charset=["b","b","b","b"],move_time=0.8,health=1,damage=1)
		self.direction = direction
		self.lifetime = 10

	def _clear_motion_lock(self):
		super()._clear_motion_lock()
		if self.parent != None:
			super().move(self.direction)
			self.lifetime -=1
			if self.lifetime <= 0:
				self.die()

	def collide_baddie(self,baddie):
		super().collide_baddie(baddie)
		self.die()

	def set_parent(self,parent):
		super().set_parent(parent)
		self.move(self.direction)
