import curses
import time
#this needs workin'
class Display:
	def __init__(self,size):
		self.size = size
		self.stdscr = None
		self.called_function = None

	#does not support color currently
	def draw(self,character,coords,color):
		for i in range(2):
			if coords[i] > self.size[i] or coords[i] < 0:
				raise IndexError("cannot execute draw(), object outside range")
			else:
				self.stdscr.addstr(coords[1],coords[0],character)

	def dostuff(self,draw_list,wait_time):
		self.stdscr.clear()

		for i in draw_list:
			self.draw(i[0],i[1],i[2])

		self.stdscr.refresh();
		time.sleep(wait_time);

		out = []
		while True:
			#k = self.stdscr.getch()
			try:
				k = self.stdscr.getkey()
				out.append(k)
			except:
				break
		return out

	def start(self):

		self.stdscr = curses.initscr()

		ys,xs = self.stdscr.getmaxyx()
		if self.size[0] > xs or self.size[1] > ys:
			self.stop()
			raise ValueError("Terminal is too small. Required at least: width "+str(self.size[0])+", height "+str(self.size[1])+" while current is of height "+str(ys)+", width "+str(xs))


		self.stdscr.nodelay(True)
		curses.noecho()
		curses.cbreak()
		self.stdscr.keypad(True)

	def stop(self):
		curses.nocbreak()
		self.stdscr.keypad(False)
		curses.echo()
		curses.endwin()
