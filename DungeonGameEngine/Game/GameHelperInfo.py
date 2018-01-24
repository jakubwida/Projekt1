from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

class GameHelperInfo(GraphicsObject):
	def __init__(self):
		""" class used in GameGraphicsObject as a child, wih information about the player. Non universal
		what is displayed on screen is passed via self.set_params
		"""
		super().__init__([0,0])

		self.params = {}
		self.params["health"]=[0,0] #[0] = current, [1] = max.    same below
		self.params["ammo"]=[0,0]
		self.params["reload"]=0.0
		self.params["weapon"]="no_weapon"

	def set_params(self,param_dict):
		""" sets the params for display. passed dict doesn't have to be complete to work."""
		for i,v in param_dict.items():
			if i in self.params.keys():
				self.params[i]=v

	def tick(self,delta_time,keys,coords):
		self._draw_health((1,1))
		self._draw_reload((1,2))
		self._draw_weapon((20,1))
		self._draw_ammo((20,2))
		bar = "="*22
		self.draw(bar,(0,4),None)

		super().tick(delta_time,keys,coords)



	def _draw_health(self,coords):
		""" as name suggests - draws health bar at coords - same with following functions"""
		h_a = self.params["health"]
		hb = "health:<"+"#"*h_a[0]+"."*(h_a[1]-h_a[0])+">"
		self.draw(hb,coords,None)

	def _draw_reload(self,coords):
		rv = self.params["reload"]
		rl = int(5.0*rv)
		rn = 5 - rl
		string = "next_bullet:<"+"#"*rl+"."*rn+">"
		self.draw(string,coords,None)

	def _draw_weapon(self,coords):
		self.draw("weapon:"+self.params["weapon"],coords,None)

	def _draw_ammo(self,coords):
		am = self.params["ammo"]
		self.draw("ammo:"+str(am[0])+"/"+str(am[1]),coords,None)
