import sys,os,pwd,shutil,subprocess,tarfile
from variables import*

def javasetup():
        x = variab()
	os.chdir(x.instPath)
	if os.listdir(x.instPath)!=[] or os.listdir(x.instPath) ==[]:
		print ("\n Downloading java install files...\n")
		subprocess.call(["wget",x.java_url])
		tar = tarfile.open(x.java_url.split('/')[-1])
		tar.extractall()
		tar.close()
	print("setting up java 1.8 update 121 ")
	shutil.copyfile("jdk-8u121-linux-x64.tar", x.oraclePath + "/jdk-8u121-linux-x64.tar")
	os.chdir(x.oraclePath)
	print("Extracting setup")
	tar = tarfile.open("jdk-8u121-linux-x64.tar")
	tar.extractall()
	tar.close()
	print("Renaming to java directory ")
	os.rename('jdk1.8.0_121','JAVA')
	print("setting up java home and PATH")
        JAVA_HOME = x.java_path
	os.environ["JAVA_HOME"] = x.java_path
	os.environ["PATH"] = JAVA_HOME + "/bin" + ":" + os.environ["PATH"]
	os.chdir(x.instPath)
	return

