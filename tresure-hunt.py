direction = input("welcome to tresure island and your aim to find tresure, you want to letf or right = ").lower()
if direction == "right":
    print("game over")
elif direction == "left":
    user_input1 = input("you want swim or weight ? swim or wait = ")
    if user_input1 == "swim":
        print("Game over")
    else:
        user_input2 = input("You want to entre red, blue or yellow door? res, yellow and blue ?   = ")
        if (user_input2) == " red" and (user_input2 == "blue"):
            print("Game over")
        else:
            print("you win the game")



