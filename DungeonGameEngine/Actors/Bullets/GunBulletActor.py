from DungeonGameEngine.Actors.BulletActor import BulletActor

class GunBulletActor(BulletActor):
	def __init__(self,coords,direction,move_time,lifetime,damage):
		super().__init__(coords,["|","|","-","-"],move_time,direction,lifetime,damage)
