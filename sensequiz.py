#Times table quiz how many can you get right???

# Import the modules needed

from random import randrange
from time import sleep
from sense_emu import SenseHat

sense = SenseHat()

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
        sense.show_message("Well done!")
        count = count+1
        
        
    else:
        print("Bad luck!!")
        sense.show_message("Bad Luck!")
        
# Displaying the final score and lights
score = str(count)
print("You scored:"  +score)
sense.show_message(score)
count = int(score)
