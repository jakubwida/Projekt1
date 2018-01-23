from DungeonGameEngine.AuthorEventEngine.AuthorEventEngine import AuthorEventEngine
from DungeonGameEngine.AuthorEventEngine.AuthorEvent import AuthorEvent

joe = "joe"
ann = "ann"
mark = "mark"


def kill_marks_events():
	print("killing marks event")
	a_e_e.remove_events_by_author(mark)

def kill_event_2():
	print("killing event 2")
	a_e_e.remove_event(event2)

def event_1_callable():
	print("event 1")

def event_2_callable():
	print("event 2")


event1 = AuthorEvent(event_1_callable,mark)
event2 = AuthorEvent(event_2_callable,joe)
event3 = AuthorEvent(kill_event_2,joe)


a_e_e = AuthorEventEngine()
a_e_e.add_event(event1,5.0)
a_e_e.add_event(event2,3.0)
a_e_e.add_event(event3,1.0)

for i in range(10):
	print(i)
	a_e_e.resolve(1.0)
