from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene

import curses

class InfoComponent(GraphicsObject):
	def __init__(self,coords,features,decorations):
		"""
 		Component displayed at the (coords) of the screen, with features such as health/mana/ammo/weapon etc.
		Passed to GameScene in constructor.
		features - > dictionary with {name:(coords,value)}
			where 	-name is what is going to be displayed on the screen
					-coords is where it will be displayed
					-value is the text to be displayed.
		decorations - > static list of texts to be displayed.
			eg. [(coords=(int,int),text=str),(...),...]
		coords - > duh, coords (x=int,y=int)
		"""
		super().__init__(coords)
		self.game_scene = None
		self.features = features
		self.decorations = decorations

	def _on_added_to_game_scene(self,GameScene):
		self.game_scene = GameScene

	def set_feature(self,feature_name,value):
		self.features[feature_name][1] = value

	def tick(self,delta_time,keys,coords):
		for k,v in self.features.items():
			self.draw(str(k)+":"+str(v[1]),v[0],None)
		for i in self.decorations:
			self.draw(i[1],i[0],None)
		super().tick(delta_time,keys,coords)
