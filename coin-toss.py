import random
toss = input("please tell us head or tail? head or tail ? = ").lower()
random_number = random.randint(0, 1)
head = 1
tail = 0
if random_number == head:
    print("you win the toss")
else:
    print("you lose the toss")




