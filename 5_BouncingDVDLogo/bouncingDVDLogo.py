# DVD players play a diagonally travelingDVD logo that bounced off the edges of the screen.
# This program simulates this colorful DVD logo by making it change direction each time it hits an edge.
# We'll also keep track of how many times a logo hits a corner of the screen.

# DO NOT RESIZE WHILE PROGRAM IS RUNNING

import sys
import random
import time

# Tries to import bext and if it can't, throws the error with a download link
try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Sets up the constant vars:
WIDTH, HEIGHT = bext.size()
# You can't print to the last column on Wiondows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 5  # (! Try changing this to 1 or 100 !)
PAUSE_AMOUNT = 0.2  # (! Try changing this to 1.0 or 0.0 !)
# (! Try changing this list to fewer colors !)
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # Generates some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Makes sure X is even so it can hit the corner
            logos[-1][X] -= 1

    # Counts how many times a logo hits the corner
    cornerBounces = 0
    # Main program loop
    while True:
        # Handles each logo in the logos list
        for logo in logos:
            # Erases the logo's current location
            bext.goto(logo[X], logo[Y])
            # (! Try commenting this out !)
            print('DVD', end='')

            originalDirection = logo[DIR]

            # Sees if the logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1

            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1

            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1

            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # Sees if the logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT

            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # Sees if the logo bounces off the right edge
            # (WIDTH - 4 because 'DVD' has 3 letters + 1 buffer space)
            elif logo[X] == WIDTH - 4 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT

            elif logo[X] == WIDTH - 4 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # Sees if the logo bounces off the top edge
            elif logo[Y] == 1 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            
            elif logo[Y] == 1 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # Sees if the logo bounces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT

            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            # Changes colors when the logo bounces
            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)

            # Moves the logo (X moves 2 because the terminal
            # characters are twice as tall as they are wide)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1

            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1

            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1

            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Displays number of corner bounces:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            # Draws the logos at their new locations
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])

        bext.goto(0, 0)

        # Required for bext-using programs
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


# If this program was run (instead of imported), run the game
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart, recreated by Scarlett Wright')
        # When Ctrl-C is pressed, end the program
        sys.exit()
