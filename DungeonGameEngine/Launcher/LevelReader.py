from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from DungeonGameEngine.Menu.MenuGraphicsObject import MenuGraphicsObject
from DungeonGameEngine.Menu.MenuText import MenuText
from DungeonGameEngine.Menu.MenuButton import MenuButton

from DungeonGameEngine.Game.GameGraphicsObject import GameGraphicsObject
from DungeonGameEngine.Game.GameHelperScene import GameHelperScene

from DungeonGameEngine.Game.GameActor import GameActor
from DungeonGameEngine.Actors.MoverActor import MoverActor

from DungeonGameEngine.Actors.WallActor import WallActor
from DungeonGameEngine.Actors.PlayerActor import PlayerActor
from DungeonGameEngine.Actors.BulletActor import BulletActor
from DungeonGameEngine.Actors.BaddieActor import BaddieActor
from DungeonGameEngine.Actors.PickupActor import PickupActor

from DungeonGameEngine.Actors.Walls.ExitWallActor import ExitWallActor
from DungeonGameEngine.Actors.Pickup.ExitPickupActor import ExitPickupActor

from DungeonGameEngine.Actors.Pickup.MGWeaponPickup import MGWeaponPickup
from DungeonGameEngine.Actors.Pickup.SniperWeaponPickup import SniperWeaponPickup
from DungeonGameEngine.Actors.Pickup.ShotgunWeaponPickup import ShotgunWeaponPickup
from DungeonGameEngine.Actors.Pickup.RocketWeaponPickup import RocketWeaponPickup
from DungeonGameEngine.Actors.Pickup.HealthPickup import HealthPickup

from DungeonGameEngine.Actors.BaddieActor import BaddieActor
import sys


class LevelReader:
	def __init__(self):
		self.default_size =  [35,15]

	def generate_level(self,size,depth,player):
		""" returns a GameGraphicsObject with GameHelperScene with given player <on perhaps different coordinates>
		level 0 is always the same
		level has no end-level and death functions set, so it has to be done manually in Launcher"""
		self.default_size = size
		if depth == 0:
			ggo = self._generate_0_level(size)
			return ggo
		else:
			return self._generate_further_level(size,depth,player)

	def _generate_0_level(self,size):
		gs = GameHelperScene([size[0],size[1]-5])
		ggo = GameGraphicsObject(gs)

		for i in range(size[1]-5):
			gs.add_child(WallActor((0,i)))
			gs.add_child(WallActor((size[0]-1,i)))

		for i in range(1,size[0]):
			gs.add_child(WallActor((i,0)))
			gs.add_child(WallActor((i,size[1]-6)))

		center_coords = (int(size[0]/2), int((size[1]-5)/2))

		player = PlayerActor(center_coords)
		#player.coords = center_coords
		gs.add_child(player)

		gs.add_child(ExitWallActor((center_coords[0],center_coords[1]+6)))

		gs.add_child(MGWeaponPickup( ( center_coords[0]+6, center_coords[1] ) ))
		gs.add_child(BaddieActor((center_coords[0]-6,center_coords[1])))
		gs.add_child(BaddieActor((center_coords[0]-7,center_coords[1])))

		#TESTING BLOCK
		gs.add_child(SniperWeaponPickup( ( center_coords[0]+6, center_coords[1]+1 ) ))
		gs.add_child(ShotgunWeaponPickup( ( center_coords[0]+6, center_coords[1]+2 ) ))
		gs.add_child(RocketWeaponPickup( ( center_coords[0]+6, center_coords[1]+3 ) ))
		gs.add_child(HealthPickup( ( center_coords[0]+6, center_coords[1]+4 ) ))
		#END BLOCK


		return ggo

	def _generate_further_level(self,size,depth,player):
		""" temporary as generation and reading not yet implemented"""
		#player = PlayerActor((10,10))
		player.coords = [12,10]
		size = self.default_size
		gs = GameHelperScene([size[0],size[1]-5])
		ggo = GameGraphicsObject(gs)
		gs.add_child(player)
		gs.add_child(ExitPickupActor((3,3)))
		return ggo


	def read_last_level(self):
		""" returns last level, and it's depth. TEMPORARY as yadda yadda reading/generating not implemented"""
		player = PlayerActor((5,5))

		size = self.default_size
		gs = GameHelperScene([size[0],size[1]-5])
		ggo = GameGraphicsObject(gs)
		gs.add_child(player)
		gs.add_child(ExitPickupActor((3,3)))
		return ggo,player,0

	def reset_level_save(self):
		""" temporary"""
		pass

	def save_level(self,level,player,depth):
		""" temporary"""
		pass
