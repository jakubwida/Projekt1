class EventEngine:
	def __init__(self):
		"""
		Class responsible for running events.
		Events can be added and removed.
		Events will be run at resolve(), which is provided with time since last running.
		Events are processed in order depending on the time given to them.
		"""
		self.events = []
		self.current_time = 0.0

	def add_event(self,event,time_till_launch):
		"""
		adds event to list.
		time_till_launch -> time at which to launch it from the moment of adding.
		"""
		added = (event,time_till_launch+self.current_time)
		self.events.append(added)


	def remove_event(self,event):
		"""
		removes event from list
		"""
		self.events = [i for i in self.events if i[0] != event ]


	def resolve(self,time_passed):
		"""
		resolves events (event.execute) that were added since last running this method.
		time_passed -> time that has passed since last runnning this method
		"""
		self._sort_events()

		last_time = self.current_time
		self.current_time = self.current_time + time_passed


		while len(self.events) > 0 and self.events[0][1] <= self.current_time:
			current_evt = self.events.pop(0)
			current_evt[0].execute()
			self._sort_events()

	def clear_events(self):
		"""removes all events. usefull at ending"""
		self.events = []

	def _sort_events(self):
		self.events = sorted(self.events, key=lambda x: x[1])
