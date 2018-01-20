from ActualGame.Actors.GameActor import GameActor

import curses

class ActorWall(GameActor):
	def __init__(self,coords):
		character = "."
		color = curses.A_STANDOUT
		super().__init__(character,coords,color)
