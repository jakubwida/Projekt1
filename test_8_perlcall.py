import subprocess
import os

var = ["80","27","testcall.txt","m","4","4"]
FNULL = open(os.devnull, 'w')
subprocess.call(['perl', 'PerlLevelGen.pl',"80","27","testcall.txt","m","4","4"],stdout=FNULL,stderr=FNULL);
