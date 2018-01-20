import curses
from ActualGame.Actors.ActorMover import ActorMover

class ActorPlayer(ActorMover):
	def __init__(self,coords):
		character = "P"
		color = curses.COLOR_BLUE
		super().__init__(character,coords,color,0.3)

	def tick(self,delta_time,keys,coords):
		km = self.game_component.keyboard_manager
		#if len(kp) > 0:
		#	f = open("log","a")
		#	f.write(str(kp)+"\n")

		if km.poll("up"):
			self.move(1)
		elif km.poll("down"):
			self.move(3)
		elif km.poll("left"):
			self.move(4)
		elif km.poll("right"):
			self.move(2)
		super().tick(delta_time,keys,coords)
