import random


def check_blackjack(user, computer):
    if sum(user) == 21 and len(user) == 2:
        print("You win with a blackjack")
        return True
    if sum(computer) == 21 and len(computer) == 2:
        print(f"Computer wins with a blackjack {sum(computer)}")
        return True
    return False


def check_user_score(user, cards):
    while True:
        if sum(user) > 21:
            if 11 in user:
                user[user.index(11)] = 1
                if sum(user) > 21:
                    print(f"You busted with score: {sum(user)}")
                    return True
            print(f"You busted with score: {sum(user)}")
            return True
        user_buy_another = input("Would you like to buy another card? (y/n): ")
        if user_buy_another.lower() != 'y':
            return False
        user.append(random.choice(cards))
        print(f"User cards: {user}, current score: {sum(user)}")


def check_computer_score(computer, cards):
    # if sum(computer) < 17:
    while sum(computer) < 17:
        computer.append(random.choice(cards))
        if sum(computer) > 21:
            print("computer busted with score: ", sum(computer))
            return True
    return False


def play():
    cards = [11, *[i for i in range(2, 10)], 10, 10, 10]
    '''user and computer will get two random cards from the cards list'''
    user = random.sample(cards, 2)
    computer = random.sample(cards, 2)
    print(f'user cards are: {user} and your current score is {sum(user)}')
    print(f'computer \'s first card is: {computer[0]}')

    '''check if user or computer has blackjack'''
    if check_blackjack(user, computer):
        return

    '''check if user score is greater than 21'''
    if check_user_score(user, cards):
        result(user, computer)
        return

    '''check if computer score is less than 17'''
    if check_computer_score(computer, cards):
        result(user, computer)
        return

    '''check result of the game'''
    result(user, computer)


def result(user, computer):
    user_total = sum(user)
    computer_total = sum(computer)

    print(f"\nFinal results:")
    print(f"Your cards: {user}, total: {user_total}")
    print(f"Computer cards: {computer}, total: {computer_total}")

    if user_total > 21:
        print("You busted. You lose!")
    elif computer_total > 21:
        print("Computer busted. You win!")
    elif user_total > computer_total:
        print("You win!")
    elif computer_total > user_total:
        print("You lose!")
    else:
        print("It's a draw!")


def main():
    while True:
        play_again = input("would you like to play 'Black Jack' game? (y/n:) ")
        if play_again.lower() != 'y':
            print("GOOD BYE")
            break
        play()


main()
