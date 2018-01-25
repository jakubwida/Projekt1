from DungeonGameEngine.Actors.PickupActor import PickupActor
from DungeonGameEngine.Weapons.SniperWeapon import SniperWeapon

class SniperWeaponPickup(PickupActor):
	def __init__(self,coords):
		super().__init__(coords,"g",self._on_picked_up)

	def _on_picked_up(self,player):
		player.weapon = SniperWeapon()
