sanjay = input("Input sanjay = \n ")
neelam = input("input neelam = \n ")
both = neelam + sanjay
both = both.lower()
print(both)
x = 0
y = 0
t = 0
ts = 0
love = "love"
true = "true"
love = list(love)
for i in love:
    x = both.count(i)
    y += x
print(f"{neelam} love score is {y}")


true = list(true)
for i in love:
    x = both.count(i)
    t += x
print(f"{neelam} true score is {t}")

over_all_total = str(y) + str(t)
print(over_all_total)

if int(over_all_total) < 10 or int(over_all_total) > 90:
    print(f"you score is {over_all_total} you go togther like cock and mentos")
elif int(over_all_total) > 50 and int(over_all_total) < 50:
    print(f"you score is {over_all_total} , you are alright togther ")
else:
    print(f"your score is {over_all_total}, you are alrigh togther")