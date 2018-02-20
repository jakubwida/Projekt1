from DungeonGameEngine.Menu.MenuText import MenuText
import curses
import re

class MenuTypeText(MenuText):
	def __init__(self,coords,text,limit):
		super().__init__(coords,text)
		self.limit = limit

	def tick(self,delta_time,keys,coords):
		super().tick(delta_time,keys,coords)
		self.check_keys(keys)

	def on_key_press(self,key):
		if self.limit > len(self.text):
			self.text = self.text+key

	def on_backspace(self):
		if len(self.text) > 0:
			self.text = self.text[:-1]

	def check_keys(self,keys):
		if len(keys) > 0:
			key = keys[0]
			if str(key) == 'KEY_BACKSPACE':
				self.on_backspace()
			elif re.match('^[a-zA-Z]$', key):
				self.on_key_press(key)
