import random

class Room:
	def __init__(self,coords_1,coords_2):
		xes = sorted([coords_1[0],coords_2[0]])
		ys = sorted([coords_1[1],coords_2[1]])
		self.coords_1 = [xes[0],ys[0]]
		self.coords_2 = [xes[1],ys[1]]

		self.area = (self.coords_2[0]-self.coords_1[0]) * (self.coords_2[1]-self.coords_1[1])
		self.center = [int((xes[1]-xes[0])/2.0),int((xes[1]-xes[0])/2.0)]


	def get_area(self):
		return self.area

	def get_boundry(self):
		boundry_1 = [ self.coords_1[i]-1 for i in range(2)]
		boundry_2 = [ self.coords_2[i]+1 for i in range(2)]
		return boundry_1,boundry_2

	def check_collision(self,other_room):
		ob1, ob2 = other_room.get_boundry()
		b1,b2 = self.get_boundry()

		return (b1[0] <= ob2[0] and b2[0] >= ob1[0] and b1[1] <= ob2[1] and b2[1] >= ob1[1])

	def get_center(self):
		return self.center

def generate_rooms(size):
	room_list = []
	covered_area = 0
	total_area = size[0]*size[1]
	target_area = int(total_area * 0.2)
	counter = 0
	max_counter =1000

	while covered_area < target_area:

		print(str(covered_area)+"/"+str(target_area)+" counter:"+str(counter))
		while(True):
			counter +=1
			if counter > max_counter:
				room_list = []
				covered_area = 0
				counter = 0
			new_coords_1 = [random.randint(0,i-1) for i in size]
			new_coords_2 = [random.randint(0,i-1) for i in size]
			new_room = Room(new_coords_1,new_coords_2)
			matches = True
			if new_room.get_area() > int(target_area*0.5) and new_room.get_area() <= new_room.coords_1[0]-new_room.coords_2[0] and new_room.get_area() <= new_room.coords_1[1]-new_room.coords_2[1]:
				continue
			for i in room_list:
				if i.check_collision(new_room):
					matches = False
					break
			if matches:
				room_list.append(new_room)
				covered_area += new_room.get_area()
				break
	mapp = [[" " for i in range(size[0])] for j in range(size[1])]
	for i,e in enumerate(room_list):
		mapp[e.coords_1[1]][e.coords_1[0]] = str(i)
		mapp[e.coords_2[1]][e.coords_2[0]] = str(i)

	for i in mapp:
		outo =""
		for j in i:
			outo += str(j)
		outo +="\n"
		print(outo)




r1 = Room((0,0),(5,5))
print(r1.get_center())
print(r1.get_area())
print(r1.get_boundry())

generate_rooms((30,40))
