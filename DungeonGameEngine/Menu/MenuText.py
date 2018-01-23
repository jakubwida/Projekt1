from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject
import curses

class MenuText(GraphicsObject):
	def __init__(self,coords,text):
		super().__init__(coords)
		self.text = text

	def tick(self,delta_time,keys,coords):
		self.draw(self.text,[0,0],None)
		super().tick(delta_time,keys,coords)
