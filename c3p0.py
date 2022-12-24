#import
import os

#varibles
callOff = False

#set starting cmd prompt
print("""   
             ad888888b,                  ,a8888a,
            d8"     "88                ,8P"'  `"Y8,
                    a8P               ,8P        Y8,
 ,adPPYba,       aad8"   8b,dPPYba,   88          88       8b,dPPYba,   8b       d8
a8"     ""       ""Y8,   88P'    "8a  88          88       88P'    "8a  `8b     d8'
8b                  "8b  88       d8  `8b        d8'       88       d8   `8b   d8'
"8a,   ,aa  Y8,     a88  88b,   ,a8"   `8ba,  ,ad8'   888  88b,   ,a8"    `8b,d8'
 `"Ybbd8"'   "Y888888P'  88`YbbdP"'      "Y8888P"     888  88`YbbdP"'       Y88'
                         88                                88               d8'
                         88                                88              d8'""")
print("Made by VTF")

#user input for callOff
userinput = input("CMD Prompt spam will be activated, call it off? (y/n)\nvictim>")

if userinput == "y":
    callOff = True
elif userinput == "n":
    callOff = False
#ask again
newInput = input("One last chance, call it off? (y/n)\nvictim>")

if newInput == "y":
    callOff = True
elif newInput == "n":
    callOff = False
    print("Your loss bud. ¯\_(!_!)_/¯")
#start new cmd and print the best tik toker of all time 
while callOff == False:
    run = "start cmd /K echo I love undertime slopper"#edit this to whatever
    os.system(run)
