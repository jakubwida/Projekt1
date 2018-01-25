from DungeonGameEngine.Actors.PickupActor import PickupActor
from DungeonGameEngine.Weapons.RocketWeapon import RocketWeapon

class RocketWeaponPickup(PickupActor):
	def __init__(self,coords):
		super().__init__(coords,"r",self._on_picked_up)

	def _on_picked_up(self,player):
		player.weapon = RocketWeapon()
