from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine

from DungeonGameEngine.Menu.MenuScene import MenuScene
from DungeonGameEngine.Menu.MenuObjectText import MenuObjectText
from DungeonGameEngine.Menu.MenuObjectButton import MenuObjectButton

from DungeonGameEngine.Game.GameScene import GameScene
from DungeonGameEngine.Game.GameComponent import GameComponent
from DungeonGameEngine.Game.InfoComponent import InfoComponent
from DungeonGameEngine.Game.Actor import Actor

dge = DungeonGameEngine()

#-------------------------

def gotogame():
	dge.set_scene(game_scene)


button1 = MenuObjectButton([10,10],"go_to_game",gotogame)
text1 = MenuObjectText([10,8],"Do you want to play?")

menu_scene = MenuScene([button1],[text1])

#---------------------

def gotomenu():
	dge.set_scene(menu_scene)

features = {"health":((0,0),"5")}
decorations = [((0,4),"#############################")]
info_component = InfoComponent((0,1),features,decorations)

game_component = GameComponent((0,6))

actor = Actor("A",(0,0),None)

game_scene = GameScene(info_component,game_component)
game_scene.set_on_escape(gotomenu)

game_component.add_actor(actor)

#--------------------


dge.set_scene(menu_scene)

dge.start()
