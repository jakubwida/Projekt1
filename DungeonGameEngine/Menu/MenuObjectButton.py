from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene

import curses

class MenuObjectButton(GraphicsObject):
	"""
	class aimed to be placed in MenuScene.
	multiple buttons are toggled via up/down arrows.
	has a callable that is run when a chosen button is pressed.
	all functions are accessible via MenuScene
	coords -> coordinates where to display itself
	text ->text to be written
	callabl -> callable callen in _on_press()
	"""
	def __init__(self,coords,text,callabl):
		super().__init__(coords)
		self.dungeon_game_engine = None
		self.text = text
		self.callabl = callabl
		self._is_highlighted = False

	def tick(self,delta_time,keys,coords):
		if self._is_highlighted == True:
			self.draw(self.text,(0,0),curses.A_BOLD)
		else:
			self.draw(self.text,(0,0),None)
		super().tick(delta_time,keys,coords)

	def highlight(self):
		""" since now, the button will change its display style to highlighted"""
		self._is_highlighted = True

	def un_highlight(self):
		""" since now, the button will change its display style to not highlighted"""
		self._is_highlighted = False

	""" to be called when MenuScene detects button press, calls "callabl" """
	def on_press(self):
		self.callabl()
