![image](https://user-images.githubusercontent.com/121358633/209449284-e217266c-7add-4206-ad6f-4c540d60044f.png)

# c3p0.py
Fair warning: ***DO NOT*** try this on a weak computer. It will fuck it up.

### How it works
I import os so within a while loop, it will spam cmd prompts with text you like. I plan to add input for that later.

### Inner workings
I have 1 important varible that protects pc's:
  + callOff

callOff is False at the start, but when user is asked for input (y/n), the callOff is determined:


<pre><code>#user input for callOff
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
</code></pre>

If callOff is false for both inputs, the following will run:
<pre><code>#start new cmd and print the best tik toker of all time 
while callOff == False:
    run = "start cmd /K echo I love undertime slopper"#edit this to whatever
    os.system(run)</code></pre>
