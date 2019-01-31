import sys,os,pwd,shutil,subprocess,tarfile
from variables import*

def invent():
    x = variab()
    #creating the base path and directories
    if not os.path.isdir(x.instPath):
        os.makedirs(x.instPath)
    #inventory stuff for new installer to inventory
    if not os.path.isdir(x.invPath):
        os.makedirs(x.invPath)
    f = open("/etc/oraInst.loc","w+")
    f.write('inventory_loc=' + x.invPath + '\ninst_group=dba')
    f.close()
    shutil.copy2("/etc/oraInst.loc",x.invPath)
    return

