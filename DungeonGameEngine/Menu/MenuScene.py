from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Scene import Scene

class MenuScene(Scene):
	def __init__(self,button_object_list=[],text_object_list=[]):
		"""
 		A scene object to be used in menus.
		Is initialised with button_object_list and text_object_list, of MenuObjectButton and MenuObjectText types, respectively.
		They will be displayed in the MenuScene.
		Pressing up/down arrows changes which one in button_object_list is highlighted.
		Pressing enter calls _on_press on highlighted button.
		button_object_list are sorted by their y coord. so that arrow keys work intuitively.
		"""
		super().__init__()
		self.text_object_list = text_object_list
		self.button_object_list = sorted(button_object_list,key = lambda x: x.coords[1])

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
				self.active_button_index -=1
			elif "KEY_DOWN" in keys:
				self.active_button_index +=1
			elif "\n" in keys:
				self.button_object_list[self.active_button_index].on_press()
				btn = self.button_object_list[self.active_button_index]
				#f = open("logg","a")
				#f.write("active index:"+str(self.active_button_index)+" button:"+btn.text+"\n")
			if self.active_button_index >= self.max_a_b_index:
				self.active_button_index = self.max_a_b_index -1
			elif self.active_button_index <0:
				self.active_button_index = 0
			self.button_object_list[self.active_button_index].highlight()



		#this uses up/down/left/right arrow regardless. So, no keyboard_manager used for flipping
		super().tick(delta_time,keys,coords)
