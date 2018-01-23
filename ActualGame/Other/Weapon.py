from ActualGame.Actors.ActorBullet import ActorBullet

class Weapon:
	def __init__(self,reload_time,mag_size,next_bullet_time,name):
		##class that is supposed to keep track of how much time is left till reload/next bullet etc, how much ammo
		#is left, and what sort of bullet to spawn
		self.current_time_delay = 0.0 # time passed since last shot, reset upon reload/rechamber
		self.reload_time = reload_time # time to reload
		self.next_bullet_time = next_bullet_time #time that is between bullets
		self.mag = [mag_size,mag_size] # [0] = current_ammo, [1] = max_ammo
		self.name = name
		self.can_shoot = True

	def tick(self,delta_time):
		self.current_time_delay += delta_time
		if self.current_time_delay >= self.next_bullet_time and self.mag[0] > 0:
			self.current_time_delay = self.next_bullet_time
			self.can_shoot =True
		elif self.current_time_delay >= self.reload_time and self.mag[0] == 0:
			self.current_time_delay = self.reload_time
			self.mag[0]=self.mag[1]
			self.can_shoot =True

	def shoot(self,coords,direction):
		if self.can_shoot:
			self.can_shoot = False
			self.mag[0]-=1
			self.current_time_delay = 0
			return self.create_bullet(coords,direction)
		else:
			return None
		#returns the bullet in said direction, zeroes the reload time left etc
		#the bullet needs to be inserted into the world by player

	def get_reload_time_frac(self):
		if self.mag[0] == 0:
			return self.current_time_delay/self.reload_time
		else:
			return self.current_time_delay/self.next_bullet_time
		#returs how much time is needed for reload in 0.0<just shot> to 1.0<reloaded/rechambered>

	def get_ammo(self):
		return self.mag
		#returns (ammo_in_mag,mag_size)

	def get_name(self):
		return self.name
		#returns name string

	def create_bullet(self,coords,direction):
		bullet = ActorBullet(coords,direction)
		return bullet
		#returns a bullet in coords, facing direction. Used in shoot()
		#TO BE OVERWRITTEN IN INHERITANCE
