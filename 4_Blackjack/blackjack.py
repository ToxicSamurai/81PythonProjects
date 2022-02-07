# Blackjack is a card game where players try to get as close to 21 points as possible without going over.
# This program uses images drawn with text characters, called ASCII art.
# American Standard Code for Information Interchange (ASCII) is a mapping of text characters to numeric codes that computers used before Unicode replaced it.

import random
import sys

# Sets up the contant vars:
HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)
BACKSIDE = 'backside'
# A list of chr codes can be found at https://inventwithpython.com/charactermap


def main():
    print('''Blackjack, by Al Sweigart, recreated by Scarlett Wright

    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value,
        (H)it to take another card.
        (s)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase you bet
        but you must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000

    # Main game loop____________________________________________________________________________________________
    while True:
        # Checks if the player has run out of money, then breaks if true
        if money <= 0:
            print("You're broke!")
            print('Thanks for playing!')
            sys.exit()

        # Let the player enter their bet (this round)
        print('Money:', money)
        bet = getBet(money)

        # Gives the dealer and the player two cards (one card = deck.pop()) from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handles player actions ________________________________________________________________________________
        print('Bet:', bet)
        # Keeps looping until player stands or busts
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            #Checks if the player has busted
            if getHandValue(playerHand) > 21:
                break
        
            # Get if the player hit, stood, or double downed
            move = getMove(playerHand, money - bet)

            # Handles the player actions ________________________________________________________________________
            if move == 'D':
                # Player is doubling down, they can increase the bet
                #Subtracts the money from the bet
                additionalBet = getBet(min(bet, (money - bet)))
                #Adds the new bet to old bet
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) < 21:
                    #The player has busted 
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn.
                break

        # Handles the dealer's actions ____________________________________________________________________________
 
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                
                if getHandValue(dealerHand) > 21:
                    #The dealer has busted
                    break
                input('Press Enter to continue...')
                print('\n\n')

        #Shows the final hands ____________________________________________________________________________________
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handles whether the player won, lost, or tied:
        if dealerValue > 21:
            print('The dealer has busted! You win ${}!'.format(bet))
            money += bet

        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet

        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet

        elif playerValue == dealerValue:
            print('It\s a tie! Your bet has been returned.')
        
        input('Press Enter to continue...')
        print('\n\n')


# __________________________________________________________________________________________________________________
def getBet(maxBet):
    # Asks the player how much they want to bet for this round
    # Keeps asking until a valid value is given
    while True:
        print('How much do you bet? (1-{} or QUIT).'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Asks again if no number was entered
        if not bet.isdecimal():
            continue

        bet = int(bet)
        # If a player entered a valid number
        if 1 <= bet <= maxBet:
            return bet


# __________________________________________________________________________________________________________________
def getDeck():
    # Returns a list of (rank, suit) tuples for all 52 cards
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            # Add the numbered cards
            deck.append((str(rank), suit))

        for rank in ('J', 'Q', 'K', 'A'):
            # Add the face and ace cards
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


# __________________________________________________________________________________________________________________
def displayHands(playerHand, dealerHand, showDealerHand):
    # Shows the player's and dealer's hands, hides the dealer's first
    # card if showDealerHand is False.
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)

    else:
        # Hides the dealer's first card:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    # Shows the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


# __________________________________________________________________________________________________________________
def getHandValue(cards):
    # Returns the value of the cards. Face cards are worth 10, aces
    # are worth 11 or 1 (this function picks the most suitable ace value).
    value = 0
    numberOfAces = 0

    # Adds the value for the non-ace cards: _________________________________________________________________________
    for card in cards:
        # Card is a tuple like (rank, suit)
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1

        # Face cards are worth 10 points
        elif rank in ('K', 'Q', 'J'):
            value += 10
        
        # Number cards are worth their number
        else:
            value += int(rank)

    # Adds the value for the aces: ________________________________________________________________________________
    # Adds 1 per ace
    value += numberOfAces
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value + 10 < 21:
            value += 10
    
    return value


# __________________________________________________________________________________________________________________
def displayCards(cards):
# Displays all the cards in the cards list
    # The text to display on each row
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        # Prints the top line of the card
        rows[0] += ' ___  '
        if card == BACKSIDE:
            # Prints a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:

            # Prints the card's front:
            # The card is a tuple data structure
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2,'_'))

    # Prinst each row on the screen:
    for row in rows:
        print(row)


# __________________________________________________________________________________________________________________
def getMove(playerHand, money):
    # Asks the player for their move, and returns 'H' for hit, 'S' for
    # stand, and 'D' for double down.
    # Keeps looping until the player enters a correct move
    while True:
        # Detemines what moves the player can make:
        moves = ['(H)it', '(S)tand', '(B)al'] # Bal is unique

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move: _________________________________________________________________________________
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        # Player has entered a valid move
        if move in ('H', 'S'):
            return move
        # Player has entered a valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move
        # UNIQUE CODE! __________________________________________________________________________________________________
        if move == 'B':
            print('You have ${}!'.format(money))

# If the program is run (instead of imported), run the game: ____________________________________________________
if __name__ == '__main__':
    main()