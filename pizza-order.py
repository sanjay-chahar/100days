pizza = input("What size pizza you want to order? S,M and L =  ")
pepperoni = input("Do you want to add pepperoni ? Y or N = ")
cheese = input("Do you want add extra cheese? Y or N = ")
price = 0
if pizza == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
       # print(f"Pizza price is £{price}")

elif pizza == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
    else:
        price += 0
elif pizza == "L":
    price += 25
    if pepperoni == "Y":
        price += 3
    else:
        price += 0
if cheese == "Y":
     price = price + 1
     print(f"Final pizz Price is £{price}")

else:
     print(f"Pizza price is £{price}")

