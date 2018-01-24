from DungeonGameEngine.Actors.MoverActor import MoverActor
import curses

class BaddieActor(MoverActor):
	def __init__(self,coords,charset=["X","X","X","X"],move_time="0.5",health=3,damage=3):
		super().__init__(coords,charset,curses.A_UNDERLINE,move_time)
		self.health = health
		self.damage = damage

	def hurt_self(self,damage):
		self.health -= damage
		if self.health <= 0:
			self.die()

	def hurt_player(self,player):
		player.hurt_self(self.damage)
		self.die()

	#collisions should be complete
	def collide_player(self,player):
		super().collide_player(player)
		self.hurt_player(player)

	def collide_bullet(self,bullet):
		super().collide_bullet(bullet)
		bullet.hurt_baddie(self)
