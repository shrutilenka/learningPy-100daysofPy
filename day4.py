import random

random_num = random.randint(1, 100)
print(random_num)

# https://www.w3schools.com/python/module_random.asp

choices = random.randint(0, 1)
if choices == 0:
    print("heads")
else:
    print("tails")

# choice = ['heads', 'tails']
# print(random.choice(choice))
