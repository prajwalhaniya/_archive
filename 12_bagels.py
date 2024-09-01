'''
Bagels, a deductive logic game.
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
'''

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    while True:
        secret_number = get_secret_num()
        number_of_guesses = 1

        while number_of_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(number_of_guesses))
                guess = input('> ')
            clues = get_clues(guess, secret_number)
            print(clues)
            number_of_guesses += 1

            if guess == secret_number:
                break
            if number_of_guesses > MAX_GUESSES:
                print('You have run out of chances to guess the number')
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    print (secret_number)
    return secret_number

def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'You got it right!!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secret_number:
            # A correct digit is in the incorrect place
            clues.append('Pico')
    
    if len(clues) == 0:
        # There are no correct clues
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()