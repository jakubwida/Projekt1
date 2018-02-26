import subprocess, os

class HighscoreCore:
	def __init__(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.dir_path = self.dir_path.replace('/DungeonGameEngine/Launcher','')


	def insert_score(self,name,score):
		subprocess.call(self.dir_path+"/HighscoreServer/HighscoreDatabase.sh insert "+str(name)+" "+str(score), shell=True)

	def get_scores(self,order,time,username=""):

		#result = subprocess.run([self.dir_path+"/HighscoreServer/HighscoreDatabase.sh get "+ str(order)+" "+str(time)+" "+str(username)], stdout=subprocess.PIPE, shell=True)
		result = subprocess.check_output([self.dir_path+"/HighscoreServer/HighscoreDatabase.sh get "+ str(order)+" "+str(time)+" "+str(username)], universal_newlines=True, shell=True)
		#list_of_results = str(result.stdout.decode('utf-8')).splitlines()
		list_of_results = result.splitlines()

		return list_of_results
