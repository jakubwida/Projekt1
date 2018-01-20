from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene
import curses

class MenuObjectText(GraphicsObject):
	""" 
	class aimed to be placed in MenuScene. displays text at coords. that's it
	coords -> coordinates where to display itself
	text ->text to be written
	"""
	def __init__(self,coords,text):
		super().__init__(coords)
		self.text = text


	def tick(self,delta_time,keys,coords):
		self.draw(self.text,(0,0),None)
		super().tick(delta_time,keys,coords)
