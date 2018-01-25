from DungeonGameEngine.Weapons.Weapon import Weapon
from DungeonGameEngine.Actors.Bullets.GunBulletActor import GunBulletActor

class ShotgunWeapon(Weapon):
	def __init__(self):
		super().__init__([5,5],0.0,30.0,10.0,"Shotgun")

	def shoot(self,player):
		super().shoot(player)
		if player.direction == "up":
			transposed = [[-1,0],[0,-1],[1,0]]
		elif player.direction == "down":
			transposed = [[-1,0],[0,1],[1,0]]
		elif player.direction == "left":
			transposed = [[0,1],[-1,0],[0,-1]]
		elif player.direction == "right":
			transposed = [[0,1],[1,0],[0,-1]]
		for j in transposed:
			newc = [player.coords[i]+j[i] for i in range(2)]
			player.spawn_actor(GunBulletActor(newc,player.direction,0.1,8,1))
