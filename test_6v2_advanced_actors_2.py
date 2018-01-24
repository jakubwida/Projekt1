from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from DungeonGameEngine.Menu.MenuGraphicsObject import MenuGraphicsObject
from DungeonGameEngine.Menu.MenuText import MenuText
from DungeonGameEngine.Menu.MenuButton import MenuButton

from DungeonGameEngine.Game.GameGraphicsObject import GameGraphicsObject
from DungeonGameEngine.Game.GameHelperScene import GameHelperScene

from DungeonGameEngine.Game.GameActor import GameActor
from DungeonGameEngine.Actors.MoverActor import MoverActor

from DungeonGameEngine.Actors.WallActor import WallActor
from DungeonGameEngine.Actors.PlayerActor import PlayerActor
from DungeonGameEngine.Actors.BulletActor import BulletActor
from DungeonGameEngine.Actors.BaddieActor import BaddieActor
from DungeonGameEngine.Actors.PickupActor import PickupActor

#reset log:
f = open("log","w")
f.write("")


def goto_game():
	ge.set_root(game)

def goto_menu(optional_arg=0):
	ge.set_root(menu)

#------------------------------------------------
button_1 = MenuButton([1,3],"goto_game",goto_game)
text_1 = MenuText([1,1],"MENU")

menu = MenuGraphicsObject([button_1],[text_1])
#------------------------------------------------

game_scene = GameHelperScene((40,22))
game = GameGraphicsObject(game_scene)
game.set_escape(goto_menu)

#------------------------------------------------

actor_moving = PlayerActor((4,6))

bullet = BulletActor((3,7))
baddie = BaddieActor((3,2))
pickup = PickupActor((12,4),"p",goto_menu)

game_scene.add_child(actor_moving)
game_scene.add_child(bullet)
game_scene.add_child(baddie)
game_scene.add_child(pickup)

for i in range(8):
	actor_stationary = WallActor((10,i))
	game_scene.add_child(actor_stationary)

#----------------------------------------------

ge = GraphicsEngine()
ge.set_root(menu)
ge.start()
