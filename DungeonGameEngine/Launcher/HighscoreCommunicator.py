from DungeonGameEngine.Menu.MenuGraphicsObject import MenuGraphicsObject
from DungeonGameEngine.Menu.MenuText import MenuText
from DungeonGameEngine.Menu.MenuButton import MenuButton
from DungeonGameEngine.Menu.MenuTypeText import MenuTypeText

from DungeonGameEngine.Launcher.HighscoreCore import HighscoreCore

class HighscoreCommunicator:
	def __init__(self,func_goto_menu,func_goto_summary):

		self.core = HighscoreCore()

		self._func_goto_menu = func_goto_menu
		self._func_goto_summary = func_goto_summary
		self._name_input_menu = self._generate_name_input_menu()
		self._name_summary_menu = self._generate_name_summary_menu()
		self._viewer_menu = self._generate_viewer_menu()



	def get_name_input_menu(self):
		return self._name_input_menu

	def get_name_summary_menu(self):
		return self._name_summary_menu

	def get_viewer_menu(self):
		return self._viewer_menu

	def _generate_name_input_menu(self):

		t1 = MenuText((3,1),"Type in your username")
		t2 = MenuText((3,2),"[A-Z] type, [BACKSPACE] erase, character limit = 128")
		self.t_highscore = MenuText((3,3),"YOUR SCORE IS: "+str(0))
		t3 = MenuText((1,5),"->")
		self.type_text = MenuTypeText((3,5),"SampleName",128)
		self.info_text = MenuText((3,6),"")

		b1 = MenuButton((3,8),"go to menu",self._func_goto_menu)
		b2 = MenuButton((3,9),"upload score",self._on_upload_pressed)
		texts = [t1,t2,self.type_text,self.info_text,t3,self.t_highscore]
		buttons = [b1,b2]

		m = MenuGraphicsObject(buttons,texts)
		self.highscore = 0

		return m

	def _generate_name_summary_menu(self):

		t1 = MenuText((3,1),"Your score has been uploaded.")
		b1 = MenuButton((3,4),"go to menu",self._func_goto_menu)

		texts = [t1]
		buttons = [b1]

		m = MenuGraphicsObject(buttons,texts)

		return m

	def _on_upload_pressed(self):
		if len(self.type_text.text) < 3:
			self.info_text.text = "name is too short, minimum 3 characters are required"
		else:
			self.info_text.text = ""
			self.core.insert_score(self.type_text.text,self.highscore)
			self._func_goto_summary()


	def set_highscore(self,highscore):
		self.t_highscore.text = "YOUR SCORE IS: "+str(highscore)
		self.highscore = highscore


	# for viewer

	def _generate_viewer_menu(self):
		t1 = MenuText((3,1),"HIGHSCORES:")

		self.highscore_viewer_text_menu_objs = []
		for i in range(10):
			t = MenuText((3,i+3),"")
			self.highscore_viewer_text_menu_objs.append(t)

		b1 = MenuButton((3,15),"go to menu",self._func_goto_menu)

		b_ord_1 = MenuButton((3,17),"top",lambda : self._request_results(0,True,None))
		b_ord_2 = MenuButton((3,18),"bottom",lambda : self._request_results(1,False,None))

		b_time_1 = MenuButton((3,20),"all time",lambda : self._request_results(2,None,"all time"))
		b_time_2 = MenuButton((3,21),"month",lambda : self._request_results(3,None,"month"))
		b_time_3  = MenuButton((3,22),"week",lambda : self._request_results(4,None,"week"))
		b_time_4  = MenuButton((3,23),"day",lambda : self._request_results(5,None,"day"))

		self.time_buttons = [b_time_1,b_time_2,b_time_3,b_time_4]
		self.ord_buttons = [b_ord_1,b_ord_2]
		self.istop = True
		self.time = "all time"


		texts = [t1]+self.highscore_viewer_text_menu_objs
		buttons = [b1]+self.time_buttons+self.ord_buttons

		m = MenuGraphicsObject(buttons,texts)

		self._request_results(1,True,None)
		self._request_results(2,None,"all time")

		return m

	def _request_results(self,caller,istop,time):
		if istop != None:
			self.istop = istop
			for i in self.ord_buttons:
				i.text = i.text.lower()
		if time != None:
			self.time = time
			for i in self.time_buttons:
				i.text = i.text.lower()
		cb = None
		if caller < 2:
			cb = self.ord_buttons[caller]
		else:
			cb = self.time_buttons[caller-2]

		cb.text = cb.text.upper()

		for i in range(10):
			self.highscore_viewer_text_menu_objs[i].text = "---"

		scores = self.core.get_scores(istop,time)
		for i,e in enumerate(scores):
			self.highscore_viewer_text_menu_objs[i].text = e

#TODO:
# actual core - fill in the skellybob
