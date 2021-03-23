import random
computer_choose = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#print(rock)
choice = int(input("What you choose ? type 0 for Rock, 1 for Paper and 2 for Scissors. =  "))
if choice == 0:
    choice = rock
elif choice == 1:
    choice = paper
elif choice == 2:
    choice = scissors
else:
    choice = choice

print(f"you choice is {choice}")


if computer_choose == 0:
    computer_choose = rock
elif computer_choose == 1:
    computer_choose = scissors
else:
    computer_choose = paper

#computer_choose = computer_choose.lower()
print(f"computer choose {computer_choose}")

if choice != rock and choice != paper and choice != scissors:
    print(f"your choice {choice} is invalid")
elif computer_choose == rock and choice == scissors:
    print("computer win")
elif computer_choose == scissors and choice == rock:
    print("You win")
elif computer_choose == scissors and choice == paper:
    print("computer win")
elif computer_choose == paper and choice == scissors:
    print("you win")
elif computer_choose == paper and choice == rock:
    print("com")
elif choice == paper and computer_choose == rock:
    print("you win")
elif computer_choose == choice:
    print("Match draw")