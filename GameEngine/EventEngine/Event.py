class Event:
	"""
	Used in Event Engine.
	callabl -> a callable that will be run when event is executed.
	"""
	def __init__(self,callabl):
		self.callable = callabl
		self.author = None #usefull hook, must be manually accessed

	""" method run when event is run in EventEngine. calls Callable passed in constructor"""
	def execute(self):
		self.callable()
