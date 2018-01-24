from DungeonGameEngine.Actors.MoverActor import MoverActor
import curses

class BulletActor(MoverActor):
	def __init__(self,coords,charset=["|","|","-","-"],move_time="0.1",direction="up",lifetime=5,damage=5):
		super().__init__(coords,charset,curses.A_DIM,move_time)
		self.damage = damage
		self.lifetime = lifetime
		self.direction = direction

	def set_parent(self,parent):
		super().set_parent(parent)
		self.new_event(self.move(direction),self,move_time)

	def _clear_motion_lock(self):
		super().move(self.direction)
		self.lifetime -= 1
		if self.lifetime ==0:
			self.die()
