import random

def get_user_choice():
    choice = input("Choose: rock, paper, or scissors: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        choice = input("Choose: rock, paper, or scissors: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win! 🎉"
    else:
        return "Computer wins! 😢"

def play():
    print("Welcome to Rock - Paper - Scissors Game!")
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        print(determine_winner(user, computer))

        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

play()
