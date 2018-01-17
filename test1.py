from GraphicsEngine import GraphicsEngine
from GraphicsEngine import GraphicsObject
from GraphicsEngine import Display

ge = GraphicsEngine.GraphicsEngine()
root = GraphicsObject.GraphicsObject()
ge.set_root(root);





class SmallInsideObject(GraphicsObject.GraphicsObject):
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
