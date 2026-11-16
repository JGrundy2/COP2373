import random

# Creates the Deck class.
class Deck():
    # Creates a function that initializes the deck using the size passed
    # into the class.
    def __init__(self, size):
        self.card_list = [i for i in range(size)]

        # Shuffles the deck.
        random.shuffle(self.card_list)

        # Keeps track of the current card.
        self.current_card = 0

        # Stores the size of the deck.
        self.size = size

    # Creates a function that deals one card from the deck.
    def deal(self):
        # Checks if there are any cards left in the deck.
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]

# Creates a function to store the card ranks and suits.
def get_cards():
    #Lists card ranks and suits found in a deck.
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J',
                 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    return ranks, suits


# Creates a function that displays the player's hand.
def display_hand(hand, ranks, suits):
    # Goes through each card in the hand.
    for i in range(len(hand)):
        d = hand[i]

        # Determines the card's rank and suit and displays this.
        r = d % 13
        s = d // 13
        print(ranks[r], 'of', suits[s])


# Creates a function that deals the original five-card hand.
def deal_hand(my_deck):
    # Creates an empty list to store the cards.
    hand = []

    # Deals the five cards from the deck.
    for i in range(5):
        d = my_deck.deal()

        # Adds each card to the hand.
        hand.append(d)
    return hand


# Creates a function that allows the user to replace selected cards.
def draw_cards(my_deck, hand):
    # Asks the user which cards they want to replace.
    choice = input('\nEnter the card numbers you want to replace (1-5), separated'
        ' by commas. Enter 0 if you do not want to replace any cards: ')

    # Checks if the user wants to keep all five cards.
    if choice.strip() == '0':
        print('\nYou kept your original cards.')
        return hand

    try:
        # Converts the user's selections into a list of numbers.
        selections = [int(card.strip()) for card in choice.split(',')]

        # Checks for duplicate numbers or numbers not that are not 1-5.
        if (len(set(selections)) != len(selections)
                or any(card < 1 or card > 5 for card in selections)):
            print('Please enter card numbers from 1 to 5.')
            return draw_cards(my_deck, hand)

        # Replaces each card selected by the user.
        for card in selections:
            hand[card - 1] = my_deck.deal()

        print('\nYour replacement cards have been dealt.')

    # Handles user input that does not have commas or is a float or string.
    except ValueError:
        print('Please enter numbers such as 1, 3, 5 (with commas). '
              'Try again.')
        return draw_cards(my_deck, hand)

    return hand


# Main program
def main():
    # Gets the ranks and suits from the get_cards function.
    ranks, suits = get_cards()

    # Creates a deck containing 52 cards.
    my_deck = Deck(52)

    # Deals the original hand.
    hand = deal_hand(my_deck)

    # Display the original hand.
    print('\nYour original Poker hand:')
    display_hand(hand, ranks, suits)

    # Allows the player to replace cards.
    hand = draw_cards(my_deck, hand)

    # Displays the final hand after possible changes.
    print('\nYour final Poker hand:')
    display_hand(hand, ranks, suits)

main()