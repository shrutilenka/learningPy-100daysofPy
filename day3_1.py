height = int(input("Enter the height: "))
age = int(input("Enter the age: "))
price = 0
if (height > 120):
    print("can ride")
    pic = input("do you want a picture? (y/n)")
    if (age < 12):
        print("$5")
        price = price + 5
    elif (age < 18):
        print("$7")
        price = price + 7
    else:
        print("$12")
        price = price + 12
    if (pic == "y" or pic == "Y" or pic == "yes" or pic == "Yes"):
        price = price+3
        print("total price is $", price)
    else:
        print("total price is $", price)
else:
    print("cannot ride")
