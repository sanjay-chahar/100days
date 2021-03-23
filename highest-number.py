#example input 78 65 89 86 55 91 64 89
highest = 0

numbers = input("please enter to find out highest number = ").split()
for number in numbers:
    number = int(number)
    if number > highest:
       highest = number
      # print(highest)


print(highest)