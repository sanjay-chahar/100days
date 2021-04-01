def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    if wall_in_front and wall_on_right():
        turn_left()
    if  front_is_clear() and right_is_clear():
        turn_right()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        jump()