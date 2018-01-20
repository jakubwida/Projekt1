from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Menu.MenuScene import MenuScene
from DungeonGameEngine.Menu.MenuObjectText import MenuObjectText
from DungeonGameEngine.Menu.MenuObjectButton import MenuObjectButton

dge = DungeonGameEngine()

text1 = MenuObjectText([1,5],"hello 1")
text2 = MenuObjectText([1,5],"hello 2")

def donothing():
	pass

def gotomenu2():
	f = open("logg",'w')
	dge.set_scene(menu2)
	f.write(str(dge.main_root.children[0].children[0].text))

def gotomenu1():
	dge.set_scene(menu1)

button1a = MenuObjectButton([1,10],"do_nothing",donothing)
button1b = MenuObjectButton([1,9],"go_to_menu_2",gotomenu2)
button2 = MenuObjectButton([1,9],"go_to_menu_1",gotomenu1)

menu1 = MenuScene([button1a,button1b],[text1])

menu2 = MenuScene([button2],[text2])

dge.set_scene(menu1)

dge.start()
