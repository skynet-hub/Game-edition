# 🃏 Blackjack Starter Template
# =============================
# Rules:
# - The deck is unlimited in size.
# - There are no Jokers.
# - Jack, Queen, and King count as 10.
# - Ace can count as 11 or 1.
# - Cards are not removed from the deck when drawn.

import random
import os  #You will use os to clear the screen when necessary
from art import logo 

print(logo)


def deal_card():
    """Return a random card from the deck."""
    # TODO: Create a list of card values and return one at random.
    pass


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # TODO: Handle blackjack (21 with 2 cards) and Ace adjustment (11 or 1)
    pass


def compare(user_score, computer_score):
    """Compare user and computer scores and return a message indicating the result."""
    # TODO: Implement the game result logic.
    pass


def play_game():
    print(logo)

    # TODO: Initialize empty lists for user_cards and computer_cards.

    # TODO: Deal two cards to each player using deal_card().

    # TODO: Display user's cards and the computer's first card.

    # TODO: Use a while loop to allow the user to draw more cards or stop.

    # TODO: Computer should draw cards until it reaches 17 or higher.

    # TODO: Call compare() to determine the outcome and print it.
    pass


# TODO: Create a loop to let the user replay the game if they choose.
