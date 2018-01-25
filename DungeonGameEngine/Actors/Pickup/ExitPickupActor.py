from DungeonGameEngine.Actors.PickupActor import PickupActor

class ExitPickupActor(PickupActor):
	def __init__(self,coords):
		super().__init__(coords,"E",self._on_picked_up)

	def _on_picked_up(self,player):
		if self.parent!= None:
			self.parent.level_end(player)
