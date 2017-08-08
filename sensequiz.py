#Times table quiz how many can you get right???

# Import the modules needed

from random import randrange
from time import sleep
from sense_emu import SenseHat

sense = SenseHat()

r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)
w = (255, 255, 255)

tick = [
b,b,b,b,b,b,g,g,
b,b,b,b,b,g,g,b,
b,b,b,b,g,g,b,b,
g,b,b,g,g,b,b,b,
g,b,g,g,b,b,b,b,
g,g,g,b,b,b,b,b,
g,g,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

cross = [
r,r,b,b,b,b,r,r,
b,r,r,b,b,r,r,b,
b,b,r,r,r,r,b,b,
b,b,b,r,r,b,b,b,
b,b,r,r,r,r,b,b,
b,r,r,b,b,r,r,b,
r,r,b,b,b,b,r,r,
b,b,b,b,b,b,b,b,
]

# Set up the score variable
count = 0
#Main game loop
for n in range (3):

#Setting up lists of numbers
    nums1 = randrange(12)
    nums2 = randrange(12)

# Converting integer to string to ask the question
    num1 = str(nums1)
    num2 = str(nums2)
    sense.show_message(num1+' x '+num2)
    attempt = input("What is " + num1 + " multiplied by "  +num2 +": ")
    #sense.show_message((nums1)(num2s))

# Converting string back to integer to calculate answer
    x = int(num1)
    y = int(num2)
    z = int(attempt)

    if z == x * y:
        print("Well Done!!")
        sense.set_pixels(tick)
        sleep(1)
        count = count+1
        
        
    else:
        print("Bad luck!!")
        sense.set_pixels(cross)
        sleep(1)
        
# Displaying the final score and lights
score = str(count)
print("You scored:"  +score)
sense.show_message(score)
count = int(score)
