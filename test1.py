from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject
from GameEngine.GraphicsEngine.Display import Display

ge = GraphicsEngine()
root = GraphicsObject()
ge.set_root(root);





class SmallInsideObject(GraphicsObject):
	def __init__(self,coords):
		super().__init__(coords)

	def tick(self,delta_time,keys,coords):
		super().tick(delta_time,keys,coords)
		if "KEY_RIGHT" in keys:
			self.coords[0]+=1;
		if "KEY_LEFT" in keys:
			self.coords[0]-=1;
		super().draw("A",(5,5),"");

smo = SmallInsideObject([4,7])

root.add_child(smo)

ge.start()
