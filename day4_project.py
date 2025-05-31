import random

print('welcome to stone paper scissors')
computer_choice = random.randint(1, 3)
human = int(input('enter your choice: 1:stone, 2:paper, 3:scissors: '))
print('human choice:', human)
print('computer choice:', computer_choice)

if human == 1 and computer_choice == 3:
    print('you win')
elif human < computer_choice:
    print('you lose')
elif human == computer_choice:
    print('draw')
else:
    print('you lose')
