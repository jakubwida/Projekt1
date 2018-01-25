from DungeonGameEngine.Actors.BulletActor import BulletActor
from DungeonGameEngine.Actors.BaddieActor import BaddieActor
class RocketBulletActor(BulletActor):
	def __init__(self,coords,direction):
		super().__init__(coords,["^","v","<",">"],1.0,direction,20,3)

	def die(self):
		if self.parent != None:
			for i in [-1,0,1]:
				for j in [-1,0,1]:
					testcoords = [self.coords[0]+i,self.coords[1]+j]
					obje = self.parent.game_map.get(testcoords)
					if isinstance(obje,BaddieActor):
						obje.hurt_self(2)
		super().die()
