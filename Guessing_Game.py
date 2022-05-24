import random


def guess(x: int):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Guess is too low')
        elif guess > random_number:
            print('Guess it to high')
    print(f'Congrats you have guessed random number {random_number} correctly')


# guess(20)

# Computer Guess as User

def computer_guess(x: int):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high because low = high
        feedback = input(f'Is {guess} too high (H), too low(L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay!! The computer guessed the number, {guess}, correctly ')


computer_guess(100)
