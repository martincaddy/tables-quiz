#Times table quiz how many can you get right???

# Import the modules needed

from random import randrange
from time import sleep
import unicornhat
from numbers import *

unicornhat.rotation(270)

def blank():
    unicornhat.clear()
    unicornhat.show()
    
def flash():
    sleep(0.2)
    blank()
    sleep(0.2)

# Set up the score variable
count = 0
#Main game loop
for n in range (6):

#Setting up lists of numbers
    nums1 = randrange(10)
    nums2 = randrange(10)

# Converting integer to string to ask the question
    num1 = str(nums1)
    num2 = str(nums2)
    attempt = input("Whats is " + num1 + " multiplied by "  +num2 +": ")

# Converting string back to integer to calculate answer
    x = int(num1)
    y = int(num2)
    z = int(attempt)

    if z == x * y:
        print("Well Done!!")
        count = count+1
        for i in range (3):
            tick()
            flash()
            
        blank()
        #for a in range(5):
##            piglow.auto_update = True
##            piglow.all(150)
##            sleep(0.1)
##            piglow.all(0)
##            sleep(0.1)

    else:
        print("Bad luck!!")
        for i in range (3):
            cross()
            flash()
            
        blank()
# Keeping score with piglow LEDs

##    if count == 1:
##        piglow.auto_update = True
##        piglow.white(200)
##
##    elif count == 2:
##        piglow.auto_update = True
##        piglow.white(200)
##        piglow.blue(200)
##
##    elif count == 3:
##        piglow.auto_update = True
##        piglow.white(200)
##        piglow.blue(200)
##        piglow.green(200)
##
##    elif count == 4:
##        piglow.auto_update = True
##        piglow.white(200)
##        piglow.blue(200)
##        piglow.green(200)
##        piglow.yellow(200)
##
##    elif count == 5:
##        piglow.auto_update = True
##        piglow.white(200)
##        piglow.blue(200)
##        piglow.green(200)
##        piglow.yellow(200)
##        piglow.orange(200)
##
##    elif count == 6:
##        piglow.auto_update = True
##        piglow.all(200)
##        

# Displaying the final score and lights
score = str(count)
print("You scored:"  +score)
count = int(score)

##if count >= 6:
##    for n in range (10):
##        piglow.auto_update = True
##        piglow.all(200)
##        sleep(0.1)
##        piglow.all(0)
##        sleep(0.1)
##
##elif count >= 4:
##    for n in range (5):
##        piglow.auto_update = True
##        piglow.white(100)
##        piglow.blue(100)
##        piglow.green(100)
##        sleep(0.1)
##        piglow.all(0)
##        sleep(0.1)
##
##else:
##    for n in range (3):
##        piglow.auto_update = True
##        piglow.white(75)
##        sleep(1)
##        piglow.white(0)
##        sleep(1)
                

