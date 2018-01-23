from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine

from DungeonGameEngine.Menu.MenuScene import MenuScene
from DungeonGameEngine.Menu.MenuObjectText import MenuObjectText
from DungeonGameEngine.Menu.MenuObjectButton import MenuObjectButton

from DungeonGameEngine.Game.GameScene import GameScene
from DungeonGameEngine.Game.GameComponent import GameComponent
from DungeonGameEngine.Game.InfoComponent import InfoComponent
from DungeonGameEngine.Game.Actor import Actor

dge = DungeonGameEngine()

from ActualGame.GameComponents.GameMapComponent import GameMapComponent
from ActualGame.GameComponents.PlayerDisplayComponent import PlayerDisplayComponent

from ActualGame.Actors.ActorPlayer import ActorPlayer
from ActualGame.Actors.ActorWall import ActorWall
from ActualGame.Actors.ActorBullet import ActorBullet
#-------------------------

def gotogame():
	dge.set_scene(game_scene)


button1 = MenuObjectButton([10,10],"go_to_game",gotogame)
text1 = MenuObjectText([10,8],"Do you want to play?")

menu_scene = MenuScene([button1],[text1])

#---------------------

def gotomenu():
	dge.set_scene(menu_scene)

player_info_comp = PlayerDisplayComponent()
game_map_comp = GameMapComponent()


game_scene = GameScene(player_info_comp,game_map_comp)

game_scene.set_on_escape(gotomenu)

player_actor = ActorPlayer((1,1))
player_wall = ActorWall((5,2))
actor_bullet = ActorBullet((5,9),1,0.8)
game_map_comp.add_actor(player_actor)
game_map_comp.add_actor(player_wall)
game_map_comp.add_actor(actor_bullet)
#--------------------


dge.set_scene(menu_scene)

dge.start()
