from DungeonGameEngine.Actors.PickupActor import PickupActor
from DungeonGameEngine.Weapons.ShotgunWeapon import ShotgunWeapon

class ShotgunWeaponPickup(PickupActor):
	def __init__(self,coords):
		super().__init__(coords,"s",self._on_picked_up)

	def _on_picked_up(self,player):
		player.weapon = ShotgunWeapon()
