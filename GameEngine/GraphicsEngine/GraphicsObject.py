
class GraphicsObject:

	def __init__(self,coords=None):
		"""creates a basic GraphicsObject.
    	coords -- (int x, int y) coordinates relative to parent GraphicsObject
    	"""
		self.parent = None
		self.children = []
		self._draw_buffer = []
		if coords != None:
			self.coords = coords
		else:
			self.coords = [0,0]
		self._GraphicsEngine = None

	def set_coords(self,coords):
		"""sets coords of graphicsObject.
    	coords -- (int x, int y) coordinates relative to parent GraphicsObject
    	"""
		self.coords = coords

	def add_child(self,graphicsObject):
		"""adds a child to GraphicsObject. Recursively sets _GraphicsEngine to children
    	graphicsObject -- a child graphicsObject to this one
    	"""
		self.children.append(graphicsObject)
		graphicsObject.set_parent(self)
		self.set_self_and_children_graphics_engine(self._GraphicsEngine)

	def remove_child(self,graphicsObject):
		"""removes a child from GraphicsObject.
    	graphicsObject -- a child graphicsObject to this one
    	"""
		graphicsObject.un_set_parent()
		self.children.remove(graphicsObject)
		graphicsObject.set_self_and_children_graphics_engine(None)

	def set_parent(self,parent):
		""" called at add_child on added child, with self as argument"""
		self.parent = parent

	def un_set_parent(self):
		""" called at remove_child on removed child"""
		self.parent = None

	def tick(self,delta_time,keys,coords):
		""" function triggered at GraphicsEngine.
    	delta_time -- float - time since last running this function
		keys - [] of keys passed since
		coords - (int x, int y) - coordinates of root relative to this object (went through all tree structure)
    	"""
		#if(len(keys) > 0):
		#	with open('log.txt', 'a') as file:
		#		file.write("tick:"+str(delta_time)+" keys:"+str(keys)+"\n");
		relativecoords = [coords[i]+self.coords[i] for i in range(2) ]
		if self._GraphicsEngine != None:
			for i in self._draw_buffer:
				oc = i[1]
				newcoords = (relativecoords[0]+oc[0],relativecoords[1]+oc[1])
				self._GraphicsEngine.draw(i[0],newcoords,i[2])

		self._draw_buffer = []

		for i in self.children:
			i.tick(delta_time,keys,relativecoords)

	def draw(self,character,coords,color):
		""" function that adds what to draw at relative coordinates to this .coords. buffered untill tick() is called.
    	character -- string - what curses character to draw
		coords -- (int x, int y) -relative coordinates to this object, where to draw
		color -- string - curses color
    	"""
		self._draw_buffer.append((character,coords,color))



	def set_self_and_children_graphics_engine(self,graphicsEngine):
		""" function that sets recursively _graphicsEngine to this objecta as well as it's children.
    	graphicsEngine -- GraphicsEngine that is to be set
    	"""
		self._GraphicsEngine = graphicsEngine
		for i in self.children:
			i.set_self_and_children_graphics_engine(graphicsEngine)
