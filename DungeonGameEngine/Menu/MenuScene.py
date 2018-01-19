from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene

class MenuScene(Scene):
	def __init__(self,button_object_list=[],text_object_list=[]):
		super().__init__()
		self.text_object_list = text_object_list
		self.button_object_list = button_object_list

		self.active_button_index = 0
		self.max_a_b_index = len(self.button_object_list)
		if(len(text_object_list)) == 0:
			self.active_button_index = None

		for i in self.text_object_list:
			self.add_child(i)

		for i in self.button_object_list:
			self.add_child(i)

	def tick(self,delta_time,keys,coords):

		if self.active_button_index != None:
			self.button_object_list[self.active_button_index].un_highlight()
			if "KEY_UP" in keys:
				self.active_button_index +=1
			elif "KEY_DOWN" in keys:
				self.active_button_index -=1
			elif "\n" in keys:
				self.button_object_list[self.active_button_index].on_press()
			if self.active_button_index >= self.max_a_b_index:
				self.active_button_index = self.max_a_b_index -1
			elif self.active_button_index <0:
				self.active_button_index = 0
			self.button_object_list[self.active_button_index].highlight()



		#this uses up/down/left/right arrow regardless. So, no keyboard_manager used for flipping
		super().tick(delta_time,keys,coords)
