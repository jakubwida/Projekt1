from DungeonGameEngine.Weapons.Weapon import Weapon
from DungeonGameEngine.Actors.Bullets.GunBulletActor import GunBulletActor

class MGWeapon(Weapon):
	def __init__(self):
		super().__init__([10,10],0.0,20.0,2.0,"Machine Gun")

	def shoot(self,player):
		super().shoot(player)
		transpos = player.dir_dict[player.direction]
		newc = [player.coords[i]+transpos[i] for i in range(2)]
		player.spawn_actor(GunBulletActor(newc,player.direction,0.1,7,1))
