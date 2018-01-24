from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

class MenuGraphicsObject(GraphicsObject):
	def __init__(self,buttons,texts):
		super().__init__([0,0])
		self.buttons = buttons
		self.texts = texts

		self.active_button_index = None
		if len(self.buttons) > 0:
			self.active_button_index = 0
		self.max_active_button_index = len(self.buttons)

		self.buttons = sorted(buttons, key = lambda x: x.coords[1])

		for i in self.buttons:
			self.add_child(i)

		for i in self.texts:
			self.add_child(i)

		self.escape = None

	def tick(self,delta_time,keys,coords):
		if "\x1b" in keys and self.escape != None:
			self.escape()
		elif self.active_button_index != None:
			self.buttons[self.active_button_index].un_highlight()
			if "\n" in keys:
				self.buttons[self.active_button_index].press()
			if "KEY_UP" in keys:
				self.active_button_index-=1
			if "KEY_DOWN" in keys:
				self.active_button_index+=1
			if self.active_button_index >= self.max_active_button_index:
				self.active_button_index = self.max_active_button_index -1
			elif self.active_button_index < 0:
				self.active_button_index = 0
			self.buttons[self.active_button_index].highlight()

		super().tick(delta_time,keys,coords)

	def set_escape(self,callabl):
		self.escape = callabl
