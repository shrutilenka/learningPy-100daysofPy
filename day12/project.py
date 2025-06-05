import random

print("ready for a guessing game?")
print("I'm thinking of a number between 1 and 100.")
computer = random.randint(1, 101)
diffi = input("choose a difficulty level: easy or hard?")
if diffi == "easy":
    attempts = 10
else:
    attempts = 5

print(f"you have {attempts} attempts remaining to guess the number")


def main():
    while True:
        global computer, attempts, diffi
        while attempts > 0:
            guess = int(input("make a guess: "))
            attempts -= 1
            if guess < computer:
                print("too low")
            elif guess > computer:
                print("too high")
            else:
                print("you got it! you win!")
                break
            print(
                f"you have {attempts} attempts remaining to guess the number")
        print(f"you lose! the number was {computer}")
        play_again = input(
            "do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("thanks for playing!")
            break


main()
