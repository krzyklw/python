import random

def play_rps_game():
    choices = ["rock", "paper", "scissors"]

    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}, to Rock, Paper, Scissors!")
    print("Choose your weapon: rock, paper, or scissors.")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(choices)

        print(f"{player_name} chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print(f"{player_name} wins!")
        else:
            print(f"{player_name} loses!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_rps_game()
