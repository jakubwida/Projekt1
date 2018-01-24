from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from DungeonGameEngine.Menu.MenuGraphicsObject import MenuGraphicsObject
from DungeonGameEngine.Menu.MenuText import MenuText
from DungeonGameEngine.Menu.MenuButton import MenuButton

from DungeonGameEngine.Game.GameGraphicsObject import GameGraphicsObject
from DungeonGameEngine.Game.GameHelperScene import GameHelperScene

def goto_game():
	ge.set_root(game)

def goto_menu():
	ge.set_root(menu)

#------------------------------------------------
button_1 = MenuButton([1,3],"goto_game",goto_game)
text_1 = MenuText([1,1],"MENU")

menu = MenuGraphicsObject([button_1],[text_1])
#------------------------------------------------

game_scene = GameHelperScene()
game = GameGraphicsObject(game_scene)
game.set_escape(goto_menu)


ge = GraphicsEngine()
ge.set_root(menu)
ge.start()
