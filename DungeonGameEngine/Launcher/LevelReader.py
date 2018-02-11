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

from DungeonGameEngine.Actors.Baddies.MineBaddieActor import MineBaddieActor
from DungeonGameEngine.Actors.Baddies.BigMineBaddieActor import BigMineBaddieActor
from DungeonGameEngine.Actors.Baddies.CrawlerBaddieActor import CrawlerBaddieActor
from DungeonGameEngine.Actors.Baddies.AmbusherBaddieActor import AmbusherBaddieActor
from DungeonGameEngine.Actors.Baddies.MotherBaddieActor import MotherBaddieActor

from DungeonGameEngine.Weapons.MGWeapon import MGWeapon
from DungeonGameEngine.Weapons.ShotgunWeapon import ShotgunWeapon
from DungeonGameEngine.Weapons.SniperWeapon import SniperWeapon
from DungeonGameEngine.Weapons.RocketWeapon import RocketWeapon

from DungeonGameEngine.Actors.BaddieActor import BaddieActor
import sys
import os
import subprocess

class LevelReader:
	def __init__(self,size):
		self.size =  size
		self.last_level_filename = "last_level.txt"
		self.current_location = os.path.dirname(os.path.realpath(__file__))
		self.current_location = self.current_location.replace("/DungeonGameEngine/Launcher","");
		f = open("log","a")
		f.write(str(self.current_location)+"\n");


	def read_last_level(self):
		""" returns last level, and it's depth. TEMPORARY as yadda yadda reading/generating not implemented"""
		exists = os.path.isfile(self.current_location+"/"+self.last_level_filename)
		if exists:
			return self._read_level(self.current_location+"/"+self.last_level_filename)
		else:
			return self._generate_0_level()

	def generate_level(self,player,depth):
		self._prod_perl_generator(self.size,player,depth)

	def reset_level_save(self):
		if os.path.isfile(self.current_location+"/"+self.last_level_filename):
			os.remove(self.current_location+"/"+self.last_level_filename)




	def _generate_0_level(self):
		gs = GameHelperScene([self.size[0],self.size[1]-5])
		ggo = GameGraphicsObject(gs)

		for i in range(self.size[1]-5):
			gs.add_child(WallActor((0,i)))
			gs.add_child(WallActor((self.size[0]-1,i)))

		for i in range(1,self.size[0]):
			gs.add_child(WallActor((i,0)))
			gs.add_child(WallActor((i,self.size[1]-6)))

		center_coords = (int(self.size[0]/2), int((self.size[1]-5)/2))

		a_player = PlayerActor(center_coords,[5,5])
		#player.coords = center_coords
		gs.add_child(a_player)
		f = open("log","a")
		f.write(str(a_player.health))
		f.write("\n")

		gs.add_child(ExitWallActor((center_coords[0],center_coords[1]+6)))

		gs.add_child(MGWeaponPickup( ( center_coords[0]+6, center_coords[1] ) ))
		gs.add_child(BaddieActor((center_coords[0]-6,center_coords[1])))
		gs.add_child(BaddieActor((center_coords[0]-7,center_coords[1])))

		#TESTING BLOCK
		#gs.add_child(SniperWeaponPickup( ( center_coords[0]+6, center_coords[1]+1 ) ))
		#gs.add_child(ShotgunWeaponPickup( ( center_coords[0]+6, center_coords[1]+2 ) ))
		#gs.add_child(RocketWeaponPickup( ( center_coords[0]+6, center_coords[1]+3 ) ))
		#gs.add_child(HealthPickup( ( center_coords[0]+6, center_coords[1]+4 ) ))

		#gs.add_child(MineBaddieActor( ( center_coords[0]+9, center_coords[1]+1 ) ))
		#gs.add_child(BigMineBaddieActor( ( center_coords[0]+9, center_coords[1]+2 ) ))
		#gs.add_child(CrawlerBaddieActor( ( center_coords[0]+9, center_coords[1]+3 ) ))
		#gs.add_child(AmbusherBaddieActor( ( center_coords[0]+9, center_coords[1]+4 ) ))
		#gs.add_child(MotherBaddieActor( ( center_coords[0]+9, center_coords[1]+5 ) ))
		#END BLOCK


		return ggo,a_player,0



	def _prod_perl_generator(self,size,player,depth):
		""" temporary """
		#ugly
		weapon = "m"
		if isinstance(player.weapon, MGWeapon):
			weapon = "m"
		elif isinstance(player.weapon, ShotgunWeapon):
			weapon = "s"
		elif isinstance(player.weapon, SniperWeapon):
			weapon = "g"
		elif isinstance(player.weapon, RocketWeapon):
			weapon = "r"

		#var = ""+str(size[0])+" "+str(size[1]-5)+" "+str(self.last_level_filename)+" "+str(weapon)+" "+str(player.health[0])+" "+str(depth)

		FNULL = open(os.devnull, 'w')
		subprocess.call(['perl', self.current_location+"/"+'PerlLevelGen.pl',str(size[0]), str(size[1]-5), str(self.current_location+"/"+self.last_level_filename), str(weapon), str(player.health[0]), str(depth)],stdout=FNULL,stderr=FNULL);

	def _read_level(self,filename):
		""" returns a GameGraphicsObject, player and depth value as a,b,c, read from filename"""
		property_dict = {"size_x":0,"size_y":0,"depth":0}
		player_dict = {"x":0,"y":0,"weapon":None,"health":0}
		weapon_dict = {"m":MGWeapon,"s":ShotgunWeapon,"g":SniperWeapon,"r":RocketWeapon}
		actor_dict = {"p+":HealthPickup,"pm":MGWeaponPickup,"ps":ShotgunWeaponPickup,"pg":SniperWeaponPickup,"pr":RocketWeaponPickup,"w":WallActor,"we":ExitWallActor, "bm":MineBaddieActor,"bM":BigMineBaddieActor,"bc":CrawlerBaddieActor,"ba":AmbusherBaddieActor,"bmo":MotherBaddieActor}

		actor_list = []

		modes = ("@property","@player","@actor")
		mode = "@property"
		f = open(filename,"r")
		for i in f.readlines():
			i = i.rstrip()
			if i in modes:
				mode = i
			else:
				if mode == "@property":
					arra = i.split()
					property_dict[arra[0]] = int(arra[1])
				elif mode == "@player":
					arra = i.split()
					player_dict[arra[0]] = arra[1]
				elif mode == "@actor":
					arra = i.split()
					coords = [int(arra[1]),int(arra[2])]
					actor = actor_dict[arra[0]](coords)
					actor_list.append(actor)

		depth = property_dict["depth"]
		size = [property_dict["size_x"],property_dict["size_y"]]
		gs = GameHelperScene([size[0],size[1]-5])
		ggo = GameGraphicsObject(gs)

		#print(depth)
		#print(size)
		#print(player_dict)
		#print(property_dict)

		player_coords = [int(player_dict["x"]),int(player_dict["y"])]

		weapon_name = player_dict["weapon"]
		#print(player_dict["weapon"])
		weapon = weapon_dict[weapon_name]()


		player = PlayerActor(player_coords)
		player.health[0] = int(player_dict["health"])
		player.weapon = weapon

		gs.add_child(player)
		for i in actor_list:
			#print(str(i.coords)+" /");
			gs.add_child(i)

		return ggo,player,depth
