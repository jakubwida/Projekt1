from DungeonGameEngine.Actors.BaddieActor import BaddieActor

class BigMineBaddieActor(BaddieActor):
	def __init__(self,coords):
		super().__init__(coords,charset=["X","X","X","X"],move_time="0.5",health=3,damage=3)
