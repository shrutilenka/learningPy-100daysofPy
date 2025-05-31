print("welcome to pizza delivery")
size = input("what size pizza do you want? s,m or l: ")
pepproni = input("do you want pepperoni? y/n: ")
extra_cheese = input("do you want extra cheese? y/n: ")
bill = 0
# if size == "s":
#     bill = bill+15
#     if pepproni == "y":
#         bill = bill+2
#     if extra_cheese == "y":
#         bill = bill+1
# elif size == "m":
#     bill = bill+20
#     if pepproni == "y":
#         bill = bill+3
#     if extra_cheese == "y":
#         bill = bill+1
# else:
#     bill = bill+25
#     if pepproni == "y":
#         bill = bill+3
#     if extra_cheese == "y":
#         bill = bill+1
# print("your final bill is $", bill)


# better code
if size == "s":
    bill = bill + 15
elif size == "m":
    bill = bill + 20
elif size == "l":
    bill = bill + 25

if pepproni == "y":
    if size == 's':
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == "y":
    bill = bill + 1
print("your final bill is $", bill)
