from DungeonGameEngine.Actors.BaddieActor import BaddieActor
from DungeonGameEngine.Actors.PlayerActor import PlayerActor
import random
import math

class AmbusherBaddieActor(BaddieActor):
	def __init__(self,coords):
		super().__init__(coords,charset=["A","A","A","A"],move_time=3.0,health=3,damage=2)
		self.player = None

	def check_line_of_sight(self):
		if self.parent != None:
			t_coords = self.player.coords
			s_coords = self.coords
			x1 = t_coords[0]
			x2 = s_coords[0]
			y1 = t_coords[1]
			y2 = s_coords[1]

			if x1 - x2 != 0:
				a = float(y2-y1)/float(x2-x1)
			else:
				a = float(y2-y1)
			b = y1 - (a * x1)
			f = open("log","a")
			f.write("t:"+str(t_coords)+" s:"+str(s_coords)+" ax+b=y a:"+str(a)+" b:"+str(b)+"\n")

			dx = math.fabs(x1-x2)
			dy = math.fabs(y1-y2)
			c_list = []
			f = open("log","a")
			if dx > dy:
				xs = min([x1,x2])
				xe = max([x1,x2])
				for x in range(xs,xe):
					c_list.append((math.floor(x),math.floor((a*x)+b)))
				f.write("dx>dy: "+str(c_list)+"\n")
			else:
				ys = min([y1,y2])
				ye = max([y1,y2])
				for y in range(ys,ye):
					c_list.append((int((y-b)/a),int(y)))
				f.write("dy>dx: "+str(c_list)+"\n")

			for i in c_list:
				elem = self.parent.game_map.get(i)

				if not(elem == None or elem == self or isinstance(elem,PlayerActor)):
					f.write("caught: : "+str(i)+" "+str(elem)+"\n")
					return False
			return True
		return False

	def get_direction_towards_player(self,player):
		dx = math.fabs(player.coords[0] -self.coords[0])
		dy = math.fabs(player.coords[1] -self.coords[1])
		if dx > dy:
			if player.coords[0] > self.coords[0]:
				return "right"
			else:
				return "left"
		else:
			if player.coords[1] > self.coords[1]:
				return "down"
			else:
				return "up"

	def set_parent(self,parent):
		super().set_parent(parent)
		for i in self.parent.children:
			if isinstance(i,PlayerActor):
				self.player = i

	def tick(self,delta_time,keys,coords):
		if self.parent != None and self.player != None:
			has_los = self.check_line_of_sight()
			if has_los:
				self.move(self.get_direction_towards_player(self.player))
		super().tick(delta_time,keys,coords)
