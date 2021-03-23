# # fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# # dirty_dozen = [fruits, vegetables]
# # print([dirty_dozen])
# # print(dirty_dozen[1][4])
# vegetables[2] = "sanjay"
# print([vegetables])
# filler = "X"

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position = list(position)
print(position)
horizontal = int(position[0])
vertical = int(position[1])
vertical_map = map[vertical - 1]
vertical_map[horizontal -1] = "XX"


# print(type(column))
# map[column][row] = ":)"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")