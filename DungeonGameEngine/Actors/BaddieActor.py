from DungeonGameEngine.Actors.MoverActor import MoverActor
import curses

class BulletActor(MoverActor):
	def __init__(self,coords,charset=["X","X","X","X"],move_time="0.5",health,damage):
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
