from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene

import curses

class MenuObjectButton(GraphicsObject):
	def __init__(self,coords,text,callabl):
		super().__init__(coords)
		self.dungeon_game_engine = None
		self.text = text
		self.callabl = callabl
		self._is_highlighted = False

	def tick(self,delta_time,keys,coords):
		if self._is_highlighted == True:
			self.draw(self.text,(0,0),None)
		else:
			self.draw(self.text,(0,0),curses.A_STANDOUT)
		super().tick(delta_time,keys,coords)

	def highlight(self):
		self._is_highlighted = True

	def un_highlight(self):
		self._is_highlighted = False

	def on_press(self):
		self.callabl()
