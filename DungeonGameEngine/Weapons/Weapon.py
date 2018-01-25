class Weapon:
	def __init__(self,ammo,current_time,reload_time,rechamber_time,name):
		self.ammo = list(ammo)
		self.current_time = current_time
		self.reload_time = reload_time
		self.rechamber_time = rechamber_time
		self.name = name

	def on_tick(self,delta_time):
		self.current_time += delta_time
		if self.ammo[0] == 0:
			if self.current_time >= self.reload_time:
				self.current_time = self.reload_time
				self.ammo[0] = self.ammo[1]
		else:
			if self.current_time >= self.rechamber_time:
				self.current_time = self.rechamber_time

	def try_shooting(self,player):
		if self.ammo[0]>0 and self.rechamber_time == self.current_time:
			self.ammo[0]-=1
			self.current_time =0
			self.shoot(player)

	#needs to be inherited, so it can spawn bullet on player depending on position
	def shoot(self,player):
		pass

	def get_time_ratio(self):
		a = self.current_time
		b = 0.0
		if self.ammo[0] == 0:
			b = self.reload_time
		else:
			b = self.rechamber_time
		f = open("log","a")
		f.write(str(a)+" "+str(b)+"\n")

		return float(a)/float(b)

	def get_ammo(self):
		return self.ammo

	def get_name(self):
		return self.name
