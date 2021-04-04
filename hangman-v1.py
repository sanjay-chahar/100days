import string
import random

word = ""
mumba = 0
winner = 0
looser = 0
while True:
    user_choice = input("How many words you want try = ")
    if not user_choice.isnumeric():
        print("Please enters only Numeric charcter")
    # user_choice = int(user_choice)
    #     elif not (isinstance(user_choice, int)):
    #         print("Please enter Numeric number only")
    elif int(user_choice) > 10:
        print("please enter numeric number and number should be less than 10")
    else:
        break
user_choice = int(user_choice)
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
print(alphabet_list)
word_randon = random.choices(alphabet_list, k=user_choice)
random_word = list(word_randon)
word_lenth = len(random_word)
print(f"print list of random word {random_word}")
while user_choice > mumba:
    mumba += 1
    question = input("please enter one letter and it should be string only = ")
    i = 0
    breaker = 0
    while True:  # i <= word_lenth:
        if question.isalpha() and len(question) == 1 and i <= word_lenth and breaker == 0:
            # print("above statment is true")
            for alphabat in random_word:
                if i <= word_lenth:
                    i += 1
                    if alphabat != question:
                        # print("wrong Great Choice")
                        looser = + 1
                        # break
                        if i == word_lenth:  # This will check all the charcters and after this print below lines
                            print("wrong Choice")

                    if alphabat == question:
                        print("Great Choice")
                        breaker = + 1
                        winner += 1
                        break
                else:
                    break

        else:  ### break will first while loop
            # counter = user_choice - mumba
            # print(f"You have only {counter} left")
            if not question.isalpha():
                print("Please enter only one alphabets charcter")
                counter = user_choice - mumba
                print(f"You have only {counter} left")
                break
            elif len(question) != 1:
                print("Please enter only one word at time no more than one word same time")
                counter = user_choice - mumba
                print(f"You have only {counter} choice left")
                break
            elif user_choice == mumba:
                if user_choice == winner:
                    # counter = user_choice - mumba
                    print("You are the winner and game finished now")
                    # print(f"You have no chice left")
                    break
                else:
                    # counter = user_choice - mumba
                    print("You loose the game now and no further choice left to play game ")
                    # print(f"You have no chice left")
                    break

            else:
                counter = user_choice - mumba
                print(f"You have only {counter} choice left now")
                break

