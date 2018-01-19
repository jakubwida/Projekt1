from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene
import curses

class MenuObjectText(GraphicsObject):
	def __init__(self,coords,text):
		super().__init__(coords)
		self.text = text


	def tick(self,delta_time,keys,coords):
		self.draw(self.text,(0,0),None)
		super().tick(delta_time,keys,coords)
