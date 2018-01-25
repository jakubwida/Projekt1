from DungeonGameEngine.Actors.PickupActor import PickupActor
from DungeonGameEngine.Weapons.MGWeapon import MGWeapon

class MGWeaponPickup(PickupActor):
	def __init__(self,coords):
		super().__init__(coords,"m",self._on_picked_up)

	def _on_picked_up(self,player):
		player.weapon = MGWeapon()
