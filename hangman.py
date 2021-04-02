import string
import random

word = ""
mumba = 0
winner = 0
looser = 0
while True:
    user_choice = input("How many words you want try = ")
    if not user_choice.isnumeric():
        print("Please enter only Numeric charcter")
    elif user_choice.isnumeric():
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
                        if i == word_lenth:
                            print("wrong Choice")

                    if alphabat == question:
                        print("Great Choice")
                        breaker = + 1
                        winner += 1
                        break
                else:
                    break

        else:  ### break will first while loop
            counter = user_choice - mumba
            print(f"You have only {counter} left")
            if user_choice == winner:
                print("You are winner won")
                break
            elif user_choice == mumba and looser > 0:
                print("You loose the game and game finished")
                break
            else:
                break




















