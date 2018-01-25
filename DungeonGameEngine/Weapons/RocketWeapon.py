from DungeonGameEngine.Weapons.Weapon import Weapon
from DungeonGameEngine.Actors.Bullets.RocketBulletActor import RocketBulletActor

class RocketWeapon(Weapon):
	def __init__(self):
		super().__init__([3,3],0.0,18.0,12.0,"Rocket Launcher")

	def shoot(self,player):
		super().shoot(player)
		transpos = player.dir_dict[player.direction]
		newc = [player.coords[i]+transpos[i] for i in range(2)]
		player.spawn_actor(RocketBulletActor(newc,player.direction))
