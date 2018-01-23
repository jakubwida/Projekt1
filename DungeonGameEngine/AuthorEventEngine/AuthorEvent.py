from GameEngine.EventEngine.Event import Event

class AuthorEvent(Event):
	"""
	Used in Author Event Engine. Inherits from EventEngine.Event
	callabl -> a callable that will be run when event is executed.
	author -> object that added the event. Used in removing the event.
	"""
	def __init__(self,callabl,author):
		super().__init__(callabl)
		self.author = author

	""" method run when event is run in AuthorEventEngine. calls Callable passed in constructor"""
	def execute(self):
		super().execute()
