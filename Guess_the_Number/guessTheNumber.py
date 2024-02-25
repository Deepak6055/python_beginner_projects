import random

import random

def guess(x):
    print("Welcome to the Guessing Game!")
    print(f"You have 3 chances to guess a number between 1 and {x}. Let's begin!")
    random_number = random.randint(1, x)
    chances = 3
    while chances > 0:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess == random_number:
            print(f'Congratulations! You\'ve cracked it! The number was indeed {random_number}!!')
            return
        elif guess < random_number:
            print("Oh no! Your guess is too low. Try aiming a bit higher!")
        elif guess > random_number:
            print("Whoa! Your guess is too high. Aim a tad lower!")
        chances -= 1
        print(f"You have {chances} {'chance' if chances == 1 else 'chances'} left.")

    print(f"Sorry, you've run out of chances! The number was {random_number}.")



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high because low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Hooray! The computer\'s guess, {guess}, was spot on!')


guess(10)
