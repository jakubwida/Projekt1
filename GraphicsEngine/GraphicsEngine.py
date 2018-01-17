import curses
import time

from GraphicsEngine.Display import Display

class GraphicsEngine:
	def __init__(self,config=None):
		"""creates a basic GraphicsEngine, setting it's configuration to confing.
    	config -- {"delta_time":float,"size":(int x, int y)} - keys are optional, default = {0.05,(80,45)}
    	"""
		self.config = {"delta_time":0.05,"size":(40,22)};
		if config != None:
			for k,v in config.items():
				self.config[k]=v

		self.root = None
		self._do_continue = True;
		self._last_time = time.clock()

		self.display = Display(self.config["size"])
		self.draw_buffer = []


	def set_root(self,graphicsObject):
		"""sets root graphicsObject of GraphicsEngine. required before starting.
		graphicsObject -- GraphicsObject that is to be set.
    	"""
		self.root = graphicsObject
		self.root.set_self_and_children_graphics_engine(self)

	def start(self):
		"""runs the loop, at every config["delta_time"] seconds.
		this calls tick() on the .root graphicsObject, with keys and delta time passed in the meantime.
		program will run untill stop() is called.
    	"""
		self.display.start()
		self._do_continue = True;
		if self.root !=None:
			try:
				while(self._do_continue):
					self._main_loop_function()
				self.display.stop()
			except:
				self.display.stop()
				raise
		else:
			raise AttributeError("root was not set.")
			#starts running. requires having called set_root() before
			#calls tick() on root. Drawn stuff appears on screen, keys pressed are passed etc.

	def stop(self):
		"""stops the loop, as soon as it is possible.
    	"""
		self.do_continue = False


	def draw(self,character,coords,color):
		""" draws the character/color at coords. coords are absolute"""
		#self.display.draw(character,coords,color)
		self.draw_buffer.append((character,coords,color))

	def _main_loop_function(self):
		""" funtion run at start()"""
		#time.sleep(self.config["delta_time"]);

		#keys = self.display.get_keys(self.config["delta_time"])

		new_time = time.clock()
		delta = new_time - self._last_time;
		self.last_time = new_time

		#self.display.clear_screen()
		keys = self.display.dostuff(self.draw_buffer,self.config["delta_time"])
		self.draw_buffer = []
		self.root.tick(delta,keys,self.root.coords)



		#self.display.refresh()
