# The Birthday Paradox is the suprisingly high probability that two people will have the same birthday even in a small group of people.
# In a group of 80 people, there's a 99.9 percent chance of two people having a matching birthday.
# But even in a group as small as 23 people, there's a 50 percent chance of a matching birthday.
# This program performs several probability experiments to determine the percentages for groups of different sizes.

import datetime
import numbers
import random


def getBirthdays(numberOfBirthdays):
    # Returns a lsit of number random date objects for birthdays
    birthdays = []

    for i in range(numberOfBirthdays):
        # The year is irrelevant, as long as the birthdays have the same year
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        # Sets birthday to the year and the date
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
    

def getMatch(birthdays):
    # Returns the date object of a birthday that occurs more than once in the birthdays list
    if len(birthdays) == len(set(birthdays)):
        # All the birthdays are unique, so return None
        return None
    
    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                # Returns the matching birthday
                return birthdayA


# Display the intro:
print('''Birthday Paradox, by Al Sweigart, recreated by Scarlett Wright

The Birthday Paradox shows us that in a group of N people, the odds that
two of them have matching birthdays is surprisingly large. This program
does a Monte Carlo simulation (that is, repeated random simulations) to
explore this concept

*Not actually a paradox
''')

# Set up a tuple of months names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# Keep asking until the user enters a valid amount
while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    # If the user puts in a valid response, set the number of birthdays to the response and break
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

# Generates and displays the birthday:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
# Uses a for loop to get the number of iterations
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Sets the month names to the birthday months
        monthName = MONTHS[birthday.month - 1]
        # Sets the date text to the month and birthday
        dateText = '{} {}'.format(monthName, birthday.day)
        # Prints ^^
        print(dateText, end='')
        # Displays a comma for each birthday after the first birthday
        print(', ', end='')
print()
print()

# Determines if there are two birthdays that match
match = getMatch(birthdays)

# Displays the results:
print('In this simulation, ', end='')
# If match doesn't equal None
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulation:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 10,000 simulation.')
# How many simulations had matching birthdays in them.
simMatch = 0
# Report on the progress every 10,000 simulations using a for loop and a modulo
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Displays the simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
