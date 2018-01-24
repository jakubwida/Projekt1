from GameEngine.GraphicsEngine.GraphicsObject import GraphicsObject

from DungeonGameEngine.Game.GameHelperInfo import GameHelperInfo

class GameGraphicsObject(GraphicsObject):
	def __init__(self,game_helper_scene):
		super().__init__([0,0])
		self.info_obj = GameHelperInfo()
		self.game_scene = game_helper_scene
		self.add_child(self.info_obj)
		self.add_child(game_helper_scene)

		self.escape = None

	def tick(self,delta_time,keys,coords):
		if self.escape != None and "\x1b" in keys:
			self.escape()

		super().tick(delta_time,keys,coords)

	def set_escape(self,callabl):
		self.escape = callabl
