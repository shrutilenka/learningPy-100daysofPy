import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '?']

print("welcome to password generator")
length = int(input("Enter the length of password: "))
sym = int(input("Enter the number of symbols: "))
nums = int(input("Enter the number of numbers: "))
alphas = length-(sym+nums)
password = []

for i in range(0, alphas):
    password.append(random.choice(letters))
for i in range(0, nums):
    password.append(random.choice(numbers))
for i in range(0, sym):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
result = ''.join(password)
print("Your password is", result)
