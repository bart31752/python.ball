# I think you should work on making a python program that
# makes a class for an object called a ball;
# give that ball 3 attributes x_coordinate, y_coordinate and radius.
# make a python script make the object and then print out its starting location,
# and then move it via a function and then print its new location.

import random
number1 = random.randint(1,9)
number2 = random.randint(1,9)

# creating a class named "Ball" with an object also called ball.
# the ball will have 3 different atributes:
# rad, x and y with values attached to them.

class Ball:   # creating a class.
    pass   # couldn't figure out what to put here yet.




ball = Ball()  # creating an object within a class.
ball.rad = 5  # giving ball some atributes.
ball.x = 0
ball.y = 0
ball.x2 = number1
ball.y2 = number2
ball.startloc = ball.x, ball.y
# for simplicity purposes i created an atribute called location,
# so it's easier to call location with just a single "input".
ball.randloc = ball.x2, ball.y2



def starting_location():
    print("Ball's starting location is: ", ball.startloc)

def random_location():
    while ball.x < ball.x2 and ball.y < ball.y2:
        print("Your new location is: ", ball.randloc)
        
# I am not satisfied with my function, as it doesnt really change ball's attribute at all
# I was supossed to change its value but I noticed that the only thing it does
# is just call for a way different value that has nothing to do with ball.x/ball.y
# As of now (14.07 8:25pm GMT +1) I will continue to search for a way to actually deal with changing the attribute value
# not only calling for something different.



starting_location()
random_location()

