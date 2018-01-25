from DungeonGameEngine.Actors.Baddies.AmbusherBaddieActor import AmbusherBaddieActor
from DungeonGameEngine.Actors.Baddies.BulletBaddieActor import BulletBaddieActor
class MotherBaddieActor(AmbusherBaddieActor):
	def __init__(self,coords):
		super().__init__(coords)
		self.charset = ["M","M","M","M"]

	def do_shooting(self):
		if self.parent!=None:
			for i in ["up","down","left","right"]:
				transposed = self.dir_dict[i]
				transposed = [transposed[i]+self.coords[i] for i in range(2)]
				self.spawn_actor(BulletBaddieActor(transposed,i))
			self.new_event(self.do_shooting,28.0)

	def set_parent(self,parent):
		super().set_parent(parent)
		self.new_event(self.do_shooting,28.0)
