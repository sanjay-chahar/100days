# ## FizzBuzz
#
# # Instructions
#
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
#
# > `Your program should print each number from 1 to 100 in turn.`
#
# >   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".`
#
# >     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#
# >       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

for number in range(1, 100):
    if number % 2 == 0 and number % 3 != 0 and number % 5 != 0:
        print(number)
    elif number % 3 == 0 and number % 5 != 0:
       print("fizz")
    elif number % 5 == 0 and number % 5 != 0:
       print("buzz")
    elif number % 3 == 0 and number % 5 == 0:
       print("fizzbuzz")
    else:
       print(number)
