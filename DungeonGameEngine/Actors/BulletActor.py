from DungeonGameEngine.Actors.MoverActor import MoverActor
import curses

class BulletActor(MoverActor):
	def __init__(self,coords,charset=["|","|","-","-"],move_time=0.1,direction="up",lifetime=6,damage=5):
		super().__init__(coords,charset,curses.A_DIM,move_time)
		self.damage = damage
		self.lifetime = lifetime
		self.direction = direction


	def set_parent(self,parent):
		super().set_parent(parent)
		self.new_event(self._clear_motion_lock,self.move_time)

	def _clear_motion_lock(self):
		super()._clear_motion_lock()
		self.lifetime -= 1
		if self.lifetime ==0:
			self.die()
		if self.parent !=None:
			super().move(self.direction)


	#can be overshadowed to not die at huting baddie
	def hurt_baddie(self,baddie):
		baddie.hurt_self(self.damage)
		self.die()


	def collide_baddie(self,baddie):
		super().collide_baddie(baddie)
		self.hurt_baddie(baddie)

	#to be overshadowed for not dying on spot
	def collide_wall(self,wall):
		super().collide_wall(wall)
		self.die()

	def collide_pickup(self,pickup):
		super().collide_pickup(pickup)
		self.die()

	def new_event(self,event,time):
		#f = open("log","a")
		#f.write("added: "+str(event)+"\n")
		super().new_event(event,time)
		#f.write("all_events:"+"\n")
		#for i in self.parent.event_engine.events:
		#	f.write(str(i[0])+":"+str(i[1])+"\n")
