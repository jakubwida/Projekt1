from GameEngine.GraphicsEngine.GraphicsEngine import GraphicsEngine
from DungeonGameEngine.Menu.MenuGraphicsObject import MenuGraphicsObject
from DungeonGameEngine.Menu.MenuText import MenuText
from DungeonGameEngine.Menu.MenuButton import MenuButton

def go_to_menu2():
	ge.set_root(menu2)

def go_to_menu1():
	ge.set_root(menu1)

def do_nothing():
	pass

button_1 = MenuButton([1,3],"goto_2",go_to_menu2)
button_2 = MenuButton([1,5],"do_nothing",do_nothing)
button_3 = MenuButton([1,3],"goto_1",go_to_menu1)

text_1 = MenuText([1,1],"MENU 1")
text_2 = MenuText([1,1],"MENU 2")

menu1 = MenuGraphicsObject([button_1,button_2],[text_1])
menu2 = MenuGraphicsObject([button_3],[text_2])
menu2.set_escape(go_to_menu1)

ge = GraphicsEngine()
ge.set_root(menu1)
ge.start()
