class Event:
	def __init__(self,callabl):
		self.callable = callabl

	def execute(self):
		self.callable()
