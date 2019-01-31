# Oracle_Healthcare_Tooling
It has code to silently install Oracle FMW , Data integrator over Linux 
Please follow below instructions to Use the tool . 
1. Make a tar file to bind various installers which are required to be downloaded when user selects an option 
2. Make changes to variables.py file which has urls of various setups to be downloaded like :
     java_url = "xyzdlakjsdkas"
     odi_122126="saklakjsldj"
     odi_12213="sklksajak"

After making changes in the variable file you may need to make changes in install.py if your tar setups has different naming than above. 

3. Run using main.py
