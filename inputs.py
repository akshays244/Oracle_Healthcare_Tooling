def inputs_in():
     
    print ("please enter the desired software version to be installerd ")
    print("Type 1 for ODI")   
    print("Type 2 for Weblogic 12.2.1.3  ")  
    product = input("Please enter .......") 
    final_input=10

    if (product==1):
        print(" Please enter  Type of ODI installation?  ")
        print ("Type 1 for standalone installation")
        print ("Type 2 for Enterprise installation ")
        odi = input("please enter ......")
        if (odi==1):
            print("Type 1 for version 12.2.1.2.6")
            print("Type 2 for version 12.2.1.3 ")
            raw_input1=input("Please enter ....")
            if(raw_input1==1):
                final_input=1
            elif(raw_input1==2):
                final_input=3
            else:
                print("wrong input ! please start the installer again")
                sys.exit()
        elif(odi==2):
            print("Type 1 for 12.2.1.2.6 ")
            print("Type 2 for 12.2.1.3 ")
            rawinput=input("Please enter ....")
            if(rawinput==1):
                final_input=2
            elif(rawinput==2):
                final_input=4
            else:
                print("wrong input")
                sys.exit();
    elif(product==2):
        print("starting Fmw 12.2.1.3 installer  .......")
        final_input = 5 
    else:
        print("Wrong input !  Please try again ")
    return final_input 
