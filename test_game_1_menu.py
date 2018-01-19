from DungeonGameEngine.DungeonGameEngine import DungeonGameEngine
from DungeonGameEngine.Menu.MenuScene import MenuScene
from DungeonGameEngine.Menu.MenuObjectText import MenuObjectText
from DungeonGameEngine.Menu.MenuObjectButton import MenuObjectButton

dge = DungeonGameEngine()

text1 = MenuObjectText([1,5],"hello")
text2 = MenuObjectText([1,6],"hello2")

def callme():
	f = open("log","a")
	f.write("callme1")

def callme2():
	f = open("log","a")
	f.write("callme2")

button = MenuObjectButton([1,8],"button1",callme)
button2 = MenuObjectButton([1,9],"button2",callme2)


main_menu = MenuScene([button,button2],[text1,text2])




#second_menu = MenuScene([button,button2],[text1,text2])

dge.set_scene(main_menu)

dge.start()
