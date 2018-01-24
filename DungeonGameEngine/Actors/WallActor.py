from DungeonGameEngine.Game.GameActor import GameActor

import curses

class WallActor(GameActor):
	def __init__(self,coords):
		super().__init__(coords,".",curses.A_STANDOUT)

	#no collision functions, as not mobile
