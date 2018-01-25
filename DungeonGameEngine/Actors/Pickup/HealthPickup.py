from DungeonGameEngine.Actors.PickupActor import PickupActor
from DungeonGameEngine.Weapons.SniperWeapon import SniperWeapon

class HealthPickup(PickupActor):
	def __init__(self,coords):
		super().__init__(coords,"+",self._on_picked_up)

	def _on_picked_up(self,player):
		if player.health[0] < player.health[1]:
			player.health[0]+=1
