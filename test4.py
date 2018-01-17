from EventEngine.EventEngine import EventEngine
from EventEngine.Event import Event

ee = EventEngine()

def callo():
	print("hello!")

def callo1():
	print("hello1!")

def callo2():
	print("hello2!")
	ee.remove_event(e2)

e1 = Event(callo)
e2 = Event(callo1)
e3 = Event(callo2)

ee.add_event(e1,1.0)
ee.add_event(e2,3.0)
ee.add_event(e3,2.0)


for i in range(10):
	print(ee.current_time)
	#print(ee.events)
	ee.resolve(0.5)
	print("--")
