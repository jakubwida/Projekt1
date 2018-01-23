import curses
from ActualGame.Actors.ActorMover import ActorMover

class ActorPlayer(ActorMover):
	def __init__(self,coords,weapon=None):
		character = "P"
		color = curses.A_BOLD
		self.weapon = None
		if weapon != None:
			self.weapon = weapon
		super().__init__(character,coords,color,0.3)

	def tick(self,delta_time,keys,coords):
		km = self.game_component.keyboard_manager
		#if len(kp) > 0:
		#	f = open("log","a")
		#	f.write(str(kp)+"\n")

		if self.weapon != None:
			self.weapon.tick(delta_time)
			ammo = self.weapon.get_ammo()
			params = {"weapon":self.weapon.get_name(),"mag":ammo[0],"mag_size":ammo[1],"reload_level":self.weapon.get_reload_time_frac()}
			self.game_scene.info_component.set_params(params)

		if km.poll("up"):
			self.move(1)
		elif km.poll("down"):
			self.move(3)
		elif km.poll("left"):
			self.move(4)
		elif km.poll("right"):
			self.move(2)
		if km.poll("shoot") and self.weapon != None and self.weapon.can_shoot:
			newpos = self._coords_dir[self.motion_dir]
			newpos = [newpos[i]+self.coords[i] for i in range(2)]
			target_place = self.game_component.game_map.get(newpos)
			bullet = self.weapon.shoot(newpos,self.motion_dir)
			f = open("log","a")
			f.write(str(bullet.coords))
			f.write(str(self.coords)+"\n")
			if target_place == None:
				self.game_component.add_actor(bullet)
		super().tick(delta_time,keys,coords)


	#needs to write shooting mechanism
