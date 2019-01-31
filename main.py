#Generalize python script to automate the install of FMW , ODI  
# Author: Akshay Sharma @ORACLE INDIA PVT LTD 

import sys,os,pwd,shutil,subprocess,tarfile 

from variables import*
from inventory import *
from inputs import inputs_in
from userset import *
from installer import install


def main():
    if not os.getuid() == 0:
        sys.exit('Script must be run as root')
    #prompt for product installation 
    invent();
    print("please specify the user to be installed from -->  0 for gbuora or 1  for oemora ")
    userinput = input("please enter  ....  ")
    user_group_check(userinput); 
    install(inputs_in());
    return 


main();

