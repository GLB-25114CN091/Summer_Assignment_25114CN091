import random

def number_guessing_game():
    print(" Number Guessing Game ")
    try:
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
        if lower >= upper:
            print("Lower bound must be less than upper bound.")
            return

        target = random.randint(lower, upper)
        attempts = 0

        while True:
            try:
                guess = int(input(f"Guess a number between {lower} and {upper}: "))
                attempts += 1

                if guess < lower or guess > upper:
                    print(f"Please enter a number within the range {lower}-{upper}.")
                elif guess < target:
                    print("Too low! Try again.")
                elif guess > target:
                    print("Too high! Try again.")
                else:
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    except ValueError:
        print("Invalid range input.")

if __name__ == "__main__":
    number_guessing_game()
