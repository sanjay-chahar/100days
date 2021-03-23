import random
names = "Sanjay, Yuvi, Neelam, Parmode, Sunita, Panda"
name_of_list = names.split()
print(name_of_list)
random_number = random.randint(0, 5)
bill = name_of_list[random_number]
print(f"today bill is paid by {bill}")
