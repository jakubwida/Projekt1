class GameMap:
	def __init__(self,size):
		self.size = size
		self.map = [[ None for i in range(size[0])] for j in range(size[1])]

	def get(self,coords):
		self.checkrange(coords)
		return self.map[coords[1]][coords[0]]

	def set(self,coords,object):
		self.checkrange(coords)
		self.map[coords[1]][coords[0]] = object

	def checkrange(self,coords):
		for i,e in enumerate(coords):
			if e > self.size[i] or e <0:
				raise IndexError("Map index outside range: index = "+str(e))
