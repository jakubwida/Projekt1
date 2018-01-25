from DungeonGameEngine.Weapons.Weapon import Weapon
from DungeonGameEngine.Actors.Bullets.GunBulletActor import GunBulletActor

class SniperWeapon(Weapon):
	def __init__(self):
		super().__init__([5,5],0.0,30.0,15.0,"Sniper Rifle")

	def shoot(self,player):
		super().shoot(player)
		transpos = player.dir_dict[player.direction]
		newc = [player.coords[i]+transpos[i] for i in range(2)]
		player.spawn_actor(GunBulletActor(newc,player.direction,0.05,25,3))
