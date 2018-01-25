from DungeonGameEngine.Actors.MoverActor import MoverActor

class PlayerActor(MoverActor):
	def __init__(self,coords,health=[5,5],weapon=None):
		"""
 		health -> [a,b] where a = current, b = max
		"""
		super().__init__(coords,["P","P","P","P"],None,0.3)
		self.weapon = None
		self.health = health

	def hurt_self(self,damage):
		self.health[0] -= damage
		if self.health[0] <= 0:
			self.die()


	#should be complete
	def collide_baddie(self,baddie):
		baddie.hurt_player(self)
		super().collide_baddie(baddie)

	def collide_pickup(self,pickup):
		temp_p = self.parent
		p_coords = pickup.coords
		pickup.get_picked_up(self)

		if temp_p == self.parent and self.parent != None:
			self.reposition(p_coords)
			super().collide_pickup(pickup)

	def tick(self,delta_time,keys,coords):
		for i in ("up","down","left","right"):
			if  self.parent != None and self.parent.keyboard_manager.poll(i):
				self.move(i)
		if self.parent != None and self.parent.keyboard_manager.poll("shoot") and self.weapon != None:
			self.weapon.try_shooting(self)

		if self.weapon != None:
			self.weapon.on_tick(delta_time)
		self._update_display()
		super().tick(delta_time,keys,coords)

	def _update_display(self):
		""" used in "tick" """
		if self.parent != None and self.parent.parent != None:
			info_obj = self.parent.parent.info_obj
			params = {}
			params["health"] = self.health
			params["ammo"] = [0,0]
			params["reload"] = 0.0
			params["weapon"] = "---"
			if self.weapon != None:
				params["ammo"] = self.weapon.get_ammo()
				params["reload"] = self.weapon.get_time_ratio()
				params["weapon"] = self.weapon.get_name()

			info_obj.set_params(params)

	def die(self):
		self.parent.death()
		super().die()
