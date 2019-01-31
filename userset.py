import sys,os,pwd,shutil,subprocess,tarfile
from executefunction import execute_command 

def changeuser(userinput):
	if(userinput==0):
		pw_rec = pwd.getpwnam("gbuora")
		gbuora_uid = pw_rec.pw_uid
		gbuora_gid = pw_rec.pw_gid
		os.setgid(gbuora_gid)
		os.setuid(gbuora_uid)
	else:
		pw_rec = pwd.getpwnam("oemora")
		oemora_uid = pw_rec.pw_uid
		oemora_gid = pw_rec.pw_gid
		os.setgid(oemora_gid)
		os.setuid(oemora_uid)

def user_setup(userinput):
	if(userinput==0):
		# setting up gbuora ownership 
                subprocess.call(["chmod","-R","775", "/scratch/stage"])
                subprocess.call(["chown","-R","gbuora:dba", "/scratch/stage"])
	elif(userinput==1):
		# setting up oemora ownership
		subprocess.call(["chmod","-R","775", "/scratch/stage"])
		subprocess.call(["chown","-R","oemora:dba", "/scratch/stage"])
	else:
		print("wrong input please enter again: ")
	return
def user_group_check(userinput):
	if(userinput==0):
		try:
			pwd.getpwnam('gbuora')
			user_setup(0);
			changeuser(0);
		except KeyError:
			print("User gbuora does not exist ! creating user and home directory")
			cmd="useradd -d /scratch/gbuora -g oinstall -G dba gbuora"
			out, err, returncode=execute_command(cmd)
			print (returncode)
			pw_rec=pwd.getpwnam("gbuora")
			gbuora_uid = pw_rec.pw_uid
			gbuora_gid = pw_rec.pw_gid
			user_setup(0);
			os.setgid(gbuora_gid)
			os.setuid(gbuora_uid)
	elif(userinput==1):
		try:
			pwd.getpwnam("oemora")
			user_setup(1);
			changeuser(1);
		except KeyError:
			print("User oemora does not exist ! creating user and home directory")
			cmd="useradd -d /scratch/oemora -g oinstall -G dba oemora"
			out, err, returncode=execute_command(cmd)
			print (returncode)
			pw_rec = pwd.getpwnam("oemora")
			oemora_uid = pw_rec.pw_uid
			oemora_gid = pw_rec.pw_gid
			user_setup(1);
			os.setgid(oemora_gid)
			os.setuid(oemora_uid)
	else:
		sys.exit("Wrong input ! Please try runnig script again ")
