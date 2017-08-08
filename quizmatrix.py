#Times table quiz how many can you get right???

# Import the modules needed

from random import randrange
from time import sleep
import unicornhat
from numbers import *

unicornhat.rotation(270)

# creating functions to show and flash images on unicornhat
def blank():
    unicornhat.clear()
    unicornhat.show()

def blink():
    sleep(0.1)
    unicornhat.clear()
    unicornhat.show()
    sleep(0.1)
    
def flash():
    sleep(0.2)
    blank()
    sleep(0.2)

# Set up the score variable
count = 0
#Main game loop
for n in range (10):

#Setting up lists of numbers
    nums1 = randrange(10)
    nums2 = randrange(10)

# Converting integer to string to ask the question
    num1 = str(nums1)
    num2 = str(nums2)
    
    if num1 == 5:
        five()
        flash()

    attempt = input("What is " + num1 + " multiplied by "  +num2 +": ")
    
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

    else:
        print("Bad luck!!")
        for i in range (3):
            cross()
            flash()
            
        blank()
# Keeping score with unicornhat
    if count == 0:
        zero()
        sleep(1)
        blank()

    elif count == 1:
        one()
        sleep(1)
        blank()

    elif count == 2:
        two()
        sleep(1)
        blank()

    elif count == 3:
        three()
        sleep(1)
        blank()

    elif count == 4:
        four()
        sleep(1)
        blank()

    elif count == 5:
        five()
        sleep(1)
        blank()

    elif count == 6:
        six()
        sleep(1)
        blank()
        
    elif count == 7:
        seven()
        sleep(1)
        blank()
        
    elif count == 8:
        eight()
        sleep(1)
        blank()
        
    elif count == 9:
        nine()
        sleep(1)
        blank()
        
    elif count == 10:
        ten()
        sleep(1)
        blank()
        
##        

# Displaying the final score and lights
score = str(count)
print("You scored:"  +score)
count = int(score)

if count == 10:
    for n in range (10):
        ten()
        blink()
        
elif count == 9:
    for n in range (10):
        nine()
        blink()
        
elif count == 8:
    for n in range (10):
        eight()
        blink()
        
elif count == 7:
    for n in range (10):
        seven()
        blink()
        
elif count == 6:
    for n in range (10):
        six()
        blink()

elif count == 5:
    for n in range (10):
        five()
        blink()

elif count == 4:
    for n in range (10):
        four()
        blink()
        
elif count == 3:
    for n in range (10):
        three()
        blink()
        
elif count == 2:
    for n in range (10):
        two()
        blink()
        
elif count == 1:
    for n in range (10):
        one()
        blink()
        
elif count == 0:
    for n in range (10):
        zero()
        blink()
