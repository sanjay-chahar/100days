sanjay = input("Input sanjay = \n ")
neelam = input("input neelam = \n ")
neelam = neelam.lower()
sanjay = sanjay.lower()
x = 0
y = 0
t = 0
ts = 0
love = "love"
true = "true"
love = list(love)
for i in love:
    x = neelam.count(i)
    y += x
print(f"{neelam} love score is {y}")
x = 0
z = 0
love = list(love)
for i in love:
    x = sanjay.count(i)
    z += x
print(f"{sanjay} love score is {z}")
love_total = str(y) + str(z)
print(f"You total love score is {love_total}")

true = list(true)
for i in love:
    x = neelam.count(i)
    t += x
print(f"{neelam} true score is {t}")
true = list(true)
for i in love:
    x = sanjay.count(i)
    ts += x
print(f"{sanjay} true score is {ts}")
true_total = str(t) + str(ts)
print(f"you total true score is {true_total}")

over_all_total = int(love_total) + int(true_total)
print(over_all_total)

if over_all_total < 10 or over_all_total > 90:
    print(f"you score is {over_all_total} you go togther like cock and mentos")
#elif over_all_total > 10 and over_all_total < 90:
 #   print(f"you score is {over_all_total} , you are alright togther ")

else:
    print(f"your score is {over_all_total}, you are alrigh togther")


