import os

class KeyboardManager:
	def __init__(self,config_file = None):
		"""
		creates keyboard manager. It will take in key lists, and return what keys have been pressed in the meantime.
		It will translate pressed keys to a set of values, with which it is initalisted, say "W" to "up"
		Initialisation creates default config, or uses one given (config_file) as filepath
		config_file -> file to be read config from
		"""
		self.config = {}
		self.config["W"] = "up"
		self.config["S"] = "down"
		self.config["A"] = "left"
		self.config["D"] = "right"
		#self.config["s_up"] = "KEY_UP"
		#self.config["s_down"] = "KEY_DOWN"
		#self.config["s_left"] = "KEY_LEFT"
		#self.config["s_right"] = "KEY_RIGHT"
		self.config[" "] = "shoot"
		self.config["E"] = "special"

		self.state = {}
		for i in self.config.values():
			self.state[i] = False

		if config_file != None:
			self.read_config(config_file)


	def read_config(self,config_file):
		"""
 		Reads confing file. File consists of lines so that name=key
		Called at initialisation if config is given
		"""
		f = open(config_file, 'r')
		lines = f.readlines()
		for l in lines:
			k,v=l.split("=")
			v=v[0:-1]
			if v in self.config.keys():
				self.config[v]=k
			else:
				raise ValueError("Keyboard configuration: key: "+v+" not found in registry")


	def write_config(self,target_filename):
		"""
 		Writes config to given filename
		"""
		if os.path.isfile(target_filename):
			os.remove(target_filename)
		f = open(target_filename,"w")
		for k,v in self.config.items():
			f.write(v+"="+k+"\n")

	def poll(self,v_key):
		"""
 		Returns True if v_key (key name) is pressed.
		v_key -> string, key name. Not key as "W" or "KEY_UP" but rather "up" or "shoot"
		"""
		if v_key in self.state.keys():
			return self.state[v_key]
		else:
			return None

	def get_keys(self):
		"""
		returns dictionary of currently pressed key names (shoot/up etc)
		"""
		return self.state

	def on_keys(self,key_list):
		"""
 		Takes in a list of keys pressed in last update, returns change list.
		Returned change list = [(string k_name,boolean val),(...)...] where k_name is shoot/up etc and val = True if pressed or False if released

		key_list -> list of key input ("W","KEY_UP" etc) from curses.
		"""
		setlist = list(set(key_list))
		v_list = [self.config[k] for k in setlist if k in self.config.keys()]
		emitted_changes = []

		for k,v in self.state.items():
			if k in v_list and v == False:
				self.state[k] = True
				emitted_changes.append((k,True))
			elif (not (k in v_list)) and v == True:
				self.state[k] = False
				emitted_changes.append((k,False))

		return emitted_changes
