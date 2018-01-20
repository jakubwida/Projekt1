from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine

from DungeonGameEngine.Menu.MenuScene import MenuScene
from DungeonGameEngine.Menu.MenuObjectText import MenuObjectText
from DungeonGameEngine.Menu.MenuObjectButton import MenuObjectButton

from DungeonGameEngine.Game.GameScene import GameScene
from DungeonGameEngine.Game.GameComponent import GameComponent
from DungeonGameEngine.Game.InfoComponent import InfoComponent
from DungeonGameEngine.Game.Actor import Actor

from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

class PlayerDisplayComponent(GraphicsObject):
	def __init__(self):
		super().__init__([0,0])
		self.params = {}
		self.params["health"] = 0
		self.params["health_max"] = 0
		self.params["reload_level"] = 0.5
		self.params["weapon"] = "no_weapon"
		self.params["mag"] = 0
		self.params["mag_size"] = 0.5

		self.wall = "-"*48


	def _on_added_to_game_scene(self,GameScene):
		self.game_scene = GameScene

	def _int_to_bar(self,val,max):
		return("<"+"#"*val+"."*(max-val)+">")

	def set_params(self,params):
		for k,v in params.items():
			if k in self.params.keys():
				self.params[k]=v


	def tick(self,delta_time,keys,coords):
		#wall
		self.draw(self.wall,(0,4),None)
		#health
		self.draw("HEALTH:"+self._int_to_bar(self.params["health"],self.params["health_max"]),(1,1),None)
		#next bullet
		self.draw("NEXT BULLET:"+self._int_to_bar(int(self.params["reload_level"]*5.0),5),(1,2),None)
		#weapon
		self.draw("WEAPON:"+self.params["weapon"],(25,1),None)
		#ammo
		self.draw("AMMUNITION:"+str(self.params["mag"])+"/"+str(self.params["mag_size"]),(25,2),None)
		super().tick(delta_time,keys,coords)
