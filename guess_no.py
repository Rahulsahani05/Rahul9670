import random

def number_guessing_game():
    print("  ------Welcome to the Number Guessing Game!------")
    print("\n       I'm thinking of a number between 1 and 100.")
    print("\n               Choose difficulty level:")
    print("\n  1. Easy   (Unlimited attempts)")
    print("  2. Medium (10 attempts)")
    print("  3. Hard   (5 attempts)")
    
    choice = input("\n Enter your choice (1/2/3): ")
    if choice == "1":
        max_attempts = None
    elif choice == "2":
        max_attempts = 10
    elif choice == "3":
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        max_attempts = 10
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess (1-100): "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
            if max_attempts and attempts >= max_attempts:
                print(f"\nGame Over! You've used all {max_attempts} attempts.")
                print(f"The correct number was {secret_number}.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
def main():
    while True:
        number_guessing_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()