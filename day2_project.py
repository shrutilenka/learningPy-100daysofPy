import math
from math import ceil

print("welcome to tip calculator")
bill_amt = float(input("what was the total bill?"))
tip = float(input("what percentage tip would you like to give? 10, 12, or 15?"))
split_bill = float(input("how many people to split the bill?"))
# each_amt = float((bill_amt+((tip*0.01)*bill_amt))/split_bill)
each_amt = round(((bill_amt+((tip*0.01)*bill_amt))/split_bill), 2)
print(f"each person should pay {each_amt}")
