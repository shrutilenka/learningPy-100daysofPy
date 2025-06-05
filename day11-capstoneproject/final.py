import random

# *[ ] is called unpacking operator
cards = [11, *[i for i in range(2, 10)], 10, 10, 10]
print(cards)
user = random.sample(cards, 2)
computer = random.sample(cards, 2)
print(f'user: {user}')
print(f'computer: {computer}')

user_buy_another = input("Would you like to buy another card? (y/n): ")
if user_buy_another.lower() == 'y':
    user.append(random.choice(cards))
    print(f"final user: {user}")
    print(f'user final sum: {sum(user)}')
else:
    print(f'user final sum: {sum(user)}')

computer_buy_another = random.choice(['y', 'n'])
print(f'computer buy another card: {computer_buy_another}')
if computer_buy_another == 'y':
    computer.append(random.choice(cards))
    print(f"final computer: {computer}")
    print(f'computer final sum: {sum(computer)}')
else:
    print(f"computer final sum: {sum(computer)}")

if sum(user) > 21 or sum(user) < sum(computer):
    print("You lose")
elif sum(user) == sum(computer):
    print("Draw")
else:
    print("You win")

    # play = input("would you like to play 'Black Jack' game? (y/n:) ")
    # if play.lower() == 'y' or play.lower() == 'yes':
    #     print("Let's play")
    # else:
    #     quit()
