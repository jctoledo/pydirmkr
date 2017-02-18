import os
import shutil
import tempfile
import time
import os
import hashlib

def deleteDir(aDir):
	shutil.rmtree(aDir)
	assert(os.path.isdir(aDir) == False)

def concatenateFiles(aDir, anOutputFile):
	'''
	read all files in aDir and add only unique lines of each file in aDir to
	anOutputFile
	'''
	#list all files 
	fout = open(anOutputFile,'w')
	fileList = [f for f in os.listdir(aDir) if os.path.isfile(os.path.join(aDir, f))]
	for f in fileList:
		linez = set()
		fin = open(os.path.join(aDir,f), 'r')
		for l in fin:
			l = l.strip()
			if len(l)>0:
				ho = hashlib.sha1(l)
				hd = ho.hexdigest()
				if hd not in linez:
					fout.write(l.strip()+"\n")
					linez.add(hd)
		fin.close()
	fout.close()



def createTempDir():
	'''
	 create a temporary directory and return the path
	'''
	
	tmpdir = tempfile.gettempdir()
	timestamp = str(int(time.time()))
	p = os.path.join(tmpdir, timestamp)
	os.makedirs(p)
	assert(os.path.isdir(p))
	return p



#d = createTempDir()
#print d
of = '/tmp/concat.test'
concatenateFiles('/var/folders/2f/q3zcxxsj6q524_4b3hgqz1nc0000gn/T/1487446900', of)
deleteDir('/var/folders/2f/q3zcxxsj6q524_4b3hgqz1nc0000gn/T/1487446900')

