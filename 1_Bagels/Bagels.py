# Bagels is a deductive loginc game in which you must guess a secret three-digit number based on clues.
# The game offers one of the following hints in reposne to your guess:
# "Pico" when your guess has a correct digit in the wrong place.
# "Fermi" when your guess has a correct digit in the correct place.
# "Bagels" if your guess has no correct digits.
# You have 10 tries to guess the secret number.

import random

NUM_DIGITS = 3  # (! Try setting this to 1 or 10 !)
MAX_GUESSES = 10  # (! Try setting this to 1 or 100!)


def main():
    print('''Bagels, a deductive logic game by Al Sweigart, recreated by Scarlett Wright
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.

    For example, if the secrect number was 248 and your guess was 843, the clues would
    be Fermi Pico.'''.format(NUM_DIGITS))  # Sets {} to NUM_DIGITS

    while True:  # Main game loop
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought of a number!')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        # numGuesses is the current number of guesses
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            # As long as guess length isn't the same as the number of digits or decimal
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('>')

            # Sets clues to the value of getClues and adds a guess
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            # If the guess is correct
            if guess == secretNum:
                break  # The number is correct, so break the loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))

        # Asks player if they want to play again
        print('Do you want to play again? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unque random digits."""
    # Creates a list of digits 0 to 9
    numbers = list('0123456889')
    # Shuffles them into a random order using random
    random.shuffle(numbers)

    # Get the first NUM_DIGITS digits in the liust for the secret number:
    secretNum = ''
    # As long as i is in range
    for i in range(NUM_DIGITS):
        # Set numbers (in string format) to secretNum (which is '' before being set) (Generates the secret number)
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, and bagels clues for a guess and secret number pair"""
    if guess == secretNum:
        return 'Correct!'

    clues = []

    for i in range(len(guess)):
        # If a number is in the correct position
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        # Else if a number is in the wrong place
        elif guess[i] in secretNum:
            clues.append('Pico')
    # If there are no correct digits
    if len(clues) == 0:
        return 'Bagels'
    else:
        # Sorts the clues into alphabetical order so their original order doesn't give the information away
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
# ngl dunno how this works
if __name__ == '__main__':
    main()
