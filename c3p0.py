#import
import os

#varibles
callOff = False

#set starting cmd prompt
print("""   
  ***                          *
 ** ***                 *     **
**   ***               **     **
**                     **     **
**                   ******** **           ****
******      ****    ********  **  ***     * ***  * *** **** ****
*****      * ***  *    **     ** * ***   *   ****   *** **** ***  *
**        *   ****     **     ***   *** **    **     **  **** ****
**       **    **      **     **     ** **    **     **   **   **
**       **    **      **     **     ** **    **     **   **   **
**       **    **      **     **     ** **    **     **   **   **
**       **    **      **     **     ** **    **     **   **   **
**       **    **      **     **     **  ******      **   **   **
**        ***** **      **    **     **   ****       ***  ***  ***
 **        ***   **            **    **               ***  ***  ***
                                     *
                                    *
                                   *
                                  *""")
print("Made by Bergua Sensua")

#user input for callOff
userinput = input("CMD Prompt spam will be activated, call it off? (y/n)\nvictim>")

if userinput == "y":
    callOff = True
else:
    callOff = False
#ask again
newInput = input("One last chance, call it off? (y/n)")

if newInput == "y":
    callOff = True
else:
    callOff = False
    print("Your loss bud. ¯\_(!_!)_/¯")
#start new cmd and print the best tik toker of all time 
while callOff == False:
    run = "start cmd /K echo I love undertime slopper"
    os.system(run)
