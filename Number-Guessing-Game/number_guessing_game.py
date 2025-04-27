import random

def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty (easy/medium/hard): ").lower()
        if difficulty == "easy":
            return 20
        elif difficulty == "medium":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid Choice. Please type easy, medium, or hard.")

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts_left = choose_difficulty()

    while attempts_left > 0:
        try :
            guess = int(input(f"Guess a number between 1 and 100 (Attempts left: {attempts_left}): "))
            attempts_left -= 1

            if guess < number_to_guess:
                print("Too Low!")
            elif guess > number_to_guess:
                print("Too High!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
                return 
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You've run out of attempts! The correct number was {number_to_guess}.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game with Difficulty Levels!")

    while True:
        play_game()
        play_again = input("|nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! GoodBye!")
            break

if __name__ == "__main__":
    number_guessing_game()


