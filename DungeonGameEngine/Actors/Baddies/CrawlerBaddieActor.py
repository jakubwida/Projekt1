from DungeonGameEngine.Actors.BaddieActor import BaddieActor
import random

class CrawlerBaddieActor(BaddieActor):
	def __init__(self,coords):
		super().__init__(coords,charset=["C","C","C","C"],move_time=1.5,health=3,damage=2)
		self.move_counter = 0
		self.direction = random.choice(("up","down","left","right"))

	def _clear_motion_lock(self):
		super()._clear_motion_lock()
		self.move_counter +=1
		self.move_time = 1.0
		if self.move_counter >= random.randint(2,3):
			self.move_counter = 0
			self.move_time = 6.0+random.random()
			self.direction = random.choice(("up","down","left","right"))
		if self.parent != None:
			self.move(self.direction)

	def set_parent(self,parent):
		super().set_parent(parent)
		self.new_event(self._clear_motion_lock,self.move_time)
