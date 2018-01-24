from DungeonGameEngine.Actors.MoverActor import MoverActor

class PlayerActor(MoverActor):
	def __init__(self,coords,health):
		"""
 		health -> [a,b] where a = current, b = max
		"""
		super().__init__(coords,["P","P","P","P"],None,0.3)
		self.weapon = None
		self.health = health

	def tick(self,delta_time,keys,coords):
		for i in ("up","down","left","right"):
			if self.parent.keyboard_manager.poll(i):
				self.move(i)
		super().tick(delta_time,keys,coords)

	def hurt_self(self,damage):
		self.health[0] -= damage
		if self.health[0] <= 0:
			self.die()
