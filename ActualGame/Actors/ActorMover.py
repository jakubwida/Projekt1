from DungeonGameEngine.Game.Actor import Actor
from GameEngine.EventEngine.Event import Event
import curses
from ActualGame.Actors.GameActor import GameActor

class ActorMover(GameActor):
	def __init__(self,character,coords,color,move_time = 0.5):
		self.move_time = move_time
		self.motion_dir = 1 # 0 = center, 1 = north, 2 = east, 3 = south, 4 = west
		self._coords_dir = {0:(0,0),1:(0,-1),2:(1,0),3:(0,1),4:(-1,0)}
		self.motion_locked = False
		super().__init__(character,coords,color)

	#move_time is the time after a motion, in which actor can't move
	def set_move_speed(self,move_time):
		self.move_time = move_time

	def move(self,direction):
		self.motion_dir = direction
		if not self.motion_locked:
			self.on_motion()
			self.motion_locked = True

	def _clear_motion_lock(self):
		#f = open("log","a")
		#f.write("lock_open!\n")
		self.motion_locked = False


	def on_motion(self):
		transp = self._coords_dir[self.motion_dir]
		newc = [self.coords[i]+transp[i] for i in range(2)]
		dest = self.game_component.game_map.get(newc)
		if dest == None:
			self.game_component.game_map.set(self.coords,None)
			self.coords = newc
			self.game_component.game_map.set(self.coords,self)
		else:
			self.collision(newc,dest)
		self.new_event(self._clear_motion_lock,self.move_time)

	def collision(self,new_coords,colliding_obj):
		pass
