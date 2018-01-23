from GameEngine.EventEngine.EventEngine import EventEngine

class AuthorEventEngine(EventEngine):
	def __init__(self):
		"""
		Class responsible for running events. inherits from EventEngine
		Events can be added and removed. They need to be created with Author <any object>
		Events will be run at resolve(), which is provided with time since last running.
		Events are processed in order depending on the time given to them.
		Events may be removed by author
		"""
		super().__init__()

	def add_event(self,event,time_till_launch):
		"""
		adds event to list.
		time_till_launch -> time at which to launch it from the moment of adding.
		"""
		super().add_event(event,time_till_launch)


	def remove_event(self,event):
		"""
		removes event from list
		"""
		super().remove_event(event)


	def resolve(self,time_passed):
		"""
		resolves events (event.execute) that were added since last running this method.
		time_passed -> time that has passed since last runnning this method
		"""
		super().resolve(time_passed)

	def clear_events(self):
		"""removes all events. usefull at ending"""
		super().clear_events()

	#NEW ONE, NOT INHERITED
	def remove_events_by_author(self,author):
		""" removes events that have a particular author"""
		self.events = [i for i in self.events if i[0].author != author]
