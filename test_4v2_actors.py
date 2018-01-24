from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from DungeonGameEngine.Menu.MenuGraphicsObject import MenuGraphicsObject
from DungeonGameEngine.Menu.MenuText import MenuText
from DungeonGameEngine.Menu.MenuButton import MenuButton

from DungeonGameEngine.Game.GameGraphicsObject import GameGraphicsObject
from DungeonGameEngine.Game.GameHelperScene import GameHelperScene

from DungeonGameEngine.Game.GameActor import GameActor

#reset log:
f = open("log","w")
f.write("")


def goto_game():
	ge.set_root(game)

def goto_menu():
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

def move_actor():
	coords = list(actor_moving.coords)
	coords[0]+=1
	actor_moving.reposition(coords)
	actor_moving.new_event(move_actor,3.0)

def kill_actor():
	game_scene.event_engine.log_events()
	actor_suicidal.die()
	game_scene.event_engine.log_events()

actor_stationary = GameActor((10,6))
actor_suicidal = GameActor((3,3))
actor_moving = GameActor((4,6))


game_scene.add_child(actor_moving)
game_scene.add_child(actor_suicidal)
game_scene.add_child(actor_stationary)

#actor_moving.new_event(move_actor,3.0)
actor_suicidal.new_event(kill_actor,1.0)
actor_moving.new_event(move_actor,2.0)

game_scene.event_engine.log_events()
#----------------------------------------------

ge = GraphicsEngine()
ge.set_root(menu)
ge.start()
