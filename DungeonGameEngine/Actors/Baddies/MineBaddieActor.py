from DungeonGameEngine.Actors.BaddieActor import BaddieActor

class MineBaddieActor(BaddieActor):
	def __init__(self,coords):
		super().__init__(coords,charset=["x","x","x","x"],move_time="0.5",health=1,damage=1)
