from DungeonGameEngine.Game.Actor import Actor
from GameEngine.EventEngine.Event import Event
import curses
from ActualGame.Actors.ActorMover import ActorMover
from ActualGame.Actors.ActorWall import ActorWall
from ActualGame.Actors.ActorBaddie import ActorBaddie

class ActorBullet(ActorMover):
	def __init__(self,coords,direction,speed=0.1,lifetime=6,charset=["-","^",">","v","<"],damage=5):
		""" lifetime is how many moves it will take untill "die()" is called. default die() just removes bullet"""
		self.lifetime = lifetime
		self.charset = charset
		self.damage=damage
		self.direction = direction

		super().__init__(charset[0],coords,curses.A_DIM)


	def on_motion(self):
		self.character = self.charset[self.motion_dir]
		super().on_motion()
		self.lifetime -=1
		if self.lifetime <= 0:
			self.die_lifetime()

	def _clear_motion_lock(self):
		super()._clear_motion_lock()
		self.move(self.direction)

	def on_added_to_game_component(self,game_component):
		super().on_added_to_game_component(game_component)
		#self._clear_motion_lock()
		#self.move(self.direction)
		self.new_event(self._clear_motion_lock,self.move_time)

	#what happens if runs out of lifetime
	def die_lifetime(self):
		if self.game_component != None:
			self.game_component.remove_actor(self)

	#what happens if hits wall
	def die_wall(self,wall_coords):
		f = open("log",'a')
		f.write("died to wall\n")
		self.game_component.remove_actor(self)

	#what happens if hits baddie
	def die_baddie(self,baddie):
		baddie.hurt_baddie(self.damage)
		self.game_component.remove_actor(self)


	def collision(self,new_coords,colliding_obj):
		#super().collision(new_coords,colliding_obj)
		if isinstance(colliding_obj,ActorWall):
			self.die_wall(new_coords)
		if isinstance(colliding_obj,ActorBaddie):
			self.die_baddie(colliding_obj)
