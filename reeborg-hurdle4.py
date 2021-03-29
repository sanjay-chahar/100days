def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    while not at_goal()and front_is_clear():
        move()
    if not at_goal() and wall_in_front() and wall_on_right():
        turn_left()
    if front_is_clear() and wall_on_right() and not at_goal():
        while not at_goal() and not right_is_clear() and front_is_clear():
             move()
    if not wall_in_front() and wall_on_right() and not at_goal():
        move()
    while not at_goal() and not wall_in_front() and wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
while not at_goal():
    jump()
