import random

def play():
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    user_choice = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    if user_choice not in choices.keys():
        print("Oops! Invalid choice. Please choose 'r' for rock, 'p' for paper, or 's' for scissors.")
        return play()

    computer_choice = random.choice(['r', 'p', 's'])

    print(f"You chose {choices[user_choice]}!")
    print(f"The computer chose {choices[computer_choice]}!")

    if user_choice == computer_choice:
        return "It's a tie!"

    if is_win(user_choice, computer_choice):
        return 'You won!'
    else:
        return 'You lost!'

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

print(play())
