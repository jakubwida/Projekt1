import subprocess, os

class HighscoreCore:
	def __init__(self):
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		self.dir_path = self.dir_path.replace('/DungeonGameEngine/Launcher','')


	def insert_score(self,name,score):
		subprocess.call(self.dir_path+"/HighscoreServer/HighscoreDatabase.sh insert "+str(name)+" "+str(score), shell=True)

	def get_scores(self,order,time,username=""):

		result = self.run([self.dir_path+"/HighscoreServer/HighscoreDatabase.sh get "+ str(order)+" "+str(time)+" "+str(username)], stdout=subprocess.PIPE, shell=True)

		list_of_results = str(result.stdout.decode('utf-8')).splitlines()

		return list_of_results

	def run(*popenargs, input=None, check=False, **kwargs):
	    if input is not None:
	        if 'stdin' in kwargs:
	            raise ValueError('stdin and input arguments may not both be used.')
	        kwargs['stdin'] = subprocess.PIPE

	    process = subprocess.Popen(*popenargs, **kwargs):
	    try:
	        stdout, stderr = process.communicate(input)
	    except:
	        process.kill()
	        process.wait()
	        raise
	    retcode = process.poll()
	    if check and retcode:
	        raise subprocess.CalledProcessError(
	            retcode, process.args, output=stdout, stderr=stderr)
	    return retcode, stdout, stderr
