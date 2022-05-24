import random
import string

from words import words


def get_valid_word(words: str) -> str:
    word = random.choice(words)  # randomly chooses something from a list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()  # what the user has guessed
    lives = 10

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letter))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # Take away live if wrong
                print('Letter is not in word')

        elif user_letter in used_letter:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You have exhausted your chances. The word was', word, '.')
    else:
        print('Congrats!! You guessed the word', word, '!!')


hangman()
