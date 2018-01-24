from DungeonGameEngine.Game.GameActor import GameActor

import curses

class PickupActor(GameActor):
	def __init__(self,coords,character,on_pickup):
		"""
 		on_pickup -> callable, called on_pickup(player) when picked up
		"""
		super().__init__(coords,character,curses.A_BLINK)
		self.on_pickup = on_pickup

	def get_picked_up(self,player):
		self.on_pickup(player)
		self.die()

	#no collision functions, as it's not mobile
