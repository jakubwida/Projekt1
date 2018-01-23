from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject
import curses

class MenuButton(GraphicsObject):
	def __init__(self,coords,text,callabl):
		super().__init__(coords)
		self.text = text
		self.color = None
		self.callabl = callabl

	def highlight(self):
		self.color = curses.A_STANDOUT

	def un_highlight(self):
		self.color = None

	def tick(self,delta_time,keys,coords):
		self.draw(self.text,[0,0],self.color)
		super().tick(delta_time,keys,coords)

	def press(self):
		self.callabl()
