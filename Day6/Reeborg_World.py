def move():
    pass
def turn_left():
    pass
def at_goal():
    pass
def front_is_clear():
    pass
def right_is_clear():
    pass
#This code can't be run Directly as it is a solution to the various challenges on Reeboorg's World Website 
# Head over to Reeborg's World -> 'https://reeborg.ca/index_en.html'

#-------------------HURDLES 1,2------------------------
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#-------------------HURDLES 3 Variable gap-----------------------
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def skip():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    while front_is_clear():
        move()
    skip()
    
#------------------------------HURDLES 4 VARIABLE GAP+HEIGHT----------
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def skip():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        skip()
    
#---------------------------MAZE--------------------------------
#Logic : Follow the right edge : Turn right if you can, if you can't then move forward, if you ca't eveen do that then turn left as a last resort
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#This loop is to cover corner cases where the robot starts off in a position with no walls around
while front_is_clear():
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    

