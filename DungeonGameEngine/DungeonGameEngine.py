from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject
from GameEngine.Util.KeyboardManager import KeyboardManager

from DungeonGameEngine.MainRoot import MainRoot

class DungeonGameEngine:
	#MainRoot is the root GraphicsObject. scene is its child, that should handle everythin from the game level
	def __init__(self):
		self.config = {"delta_time":0.05,"size":(48,27)}
		self.graphics_engine = GraphicsEngine(self.config)
		self.main_root = MainRoot(self)
		self.graphics_engine.set_root(self.main_root)

		self.keyboard_manager = KeyboardManager()
		self.last_keys_pressed = []

		self.scene = None

	#PRIVATE: run by MainRoot, on tick, to interact with .keyboard_manager
	def _pass_keys(self,keys):
		self.last_keys_pressed = self.keyboard_manager.on_keys(keys)

	def start(self):
		self.graphics_engine.start()

	def stop(self):
		self.graphics_engine.stop()

	#adds scene (GraphicsObject) to MainRoot
	def set_scene(self,scene):
		self.scene = scene
		self.main_root.set_scene(scene)
