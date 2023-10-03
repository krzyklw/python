import random
import webbrowser

def play_game():
    target_number = random.randint(1, 5)
    user_guess = int(input("Guess a number between 1 and 5: "))

    if user_guess == target_number:
        print("You won")
    else:
        print("You lose the answer is " + str(target_number))
        webbrowser.open("https://www.youtube.com/watch?v=p7YXXieghto")

play_game()