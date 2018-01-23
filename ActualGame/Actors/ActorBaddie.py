from DungeonGameEngine.Game.Actor import Actor
from GameEngine.EventEngine.Event import Event
import curses
from ActualGame.Actors.ActorMover import ActorMover
from ActualGame.Actors.ActorWall import ActorWall
from ActualGame.Actors.ActorPlayer import ActorPlayer

#STUB
class ActorBaddie(ActorMover):
	def __init__(self,coords):
		super().__init__("c",coords,curses.A_UNDERLINE)

	def hurt_baddie(self):
		pass
