from DungeonGameEngine.Game.GameActor import GameActor

class MoverActor(GameActor):
	def __init__(self,coords,charset=["^","v","<",">"],color=None,move_time=0.5):
		"""Actor that moves in given speed. Base for player, bullet etc
		charset -> set of characters to be taken when moving in directions
		color -> as usual
		move_time -> time after moving, after waiting which, object will be able to move again"""
		self.charset =charset
		self.move_time = move_time

		self.key_list = ("up","down","left","right")
		self.direction = "up" #default
		self.dir_dict = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}
		self.movement_lock = False

		super().__init__(coords,charset[0],color)


	def move(self,direction):
		"""called when object needs to move.
		direction -> string, "up" "down" "left" "right", pointing towards the desired direction """
		self.direction = direction
		self.character = self.charset[self.key_list.index(direction)]
		if not self.movement_lock:
			self._do_move(self.direction)
			self.movement_lock = True

	def _do_move(self,direction):
		transpos = self.dir_dict[direction]
		new_coords = [e+transpos[i] for i,e in enumerate(self.coords)]
		self.reposition(new_coords)
		if self.parent !=None:
			self.new_event(self._clear_motion_lock,self.move_time)

	def _clear_motion_lock(self):
		self.movement_lock = False
