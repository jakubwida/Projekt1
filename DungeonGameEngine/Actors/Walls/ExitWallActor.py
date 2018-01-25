from DungeonGameEngine.Actors.WallActor import WallActor

class ExitWallActor(WallActor):
	def __init__(self,coords):
		super().__init__(coords)
		self.character = "E"

	#no collision functions, as not mobile
