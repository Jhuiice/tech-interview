# CTCI 7.1 Deck Of Cards

from collections import deque
from random import shuffle
# ? Design the data structures for a generic deck of cards. Explain how you would subclass the data strcutures to implement blackjack

# What can we do with a deck of cards
# shuffle
# top card
# break
# random card?
# how do we show specific values of the cards.
# Hearts, Diamonds, Clubs, Spades
# 2-10 Jack, Queen, King, Ace
# we can hard code this into a dictionary or place them all into an array as tuples?
# ( [2-12 | Jack | Queen | King | Ace], Hearts | Diamonds | Clubs | Spades ) * 52
deck = [
    ("2", "Diamonds"), ("3", "diamonds"), ("4", "diamonds"),
    ("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"),
    ("8", "diamonds"), ("9", "diamonds"), ("10", "diamonds"),
    ("Jack", "hearts"), ("Queen", "hearts"), ("King", "hearts"),
    ("Ace", "hearts"), ("2", "hearts"), ("3", "hearts"), ("4", "hearts"),
    ("5", "hearts"), ("6", "hearts"), ("7", "hearts"),
    ("8", "hearts"), ("9", "hearts"), ("10", "hearts"),
    ("Jack", "hearts"), ("Queen", "hearts"), ("King", "hearts"),
    ("Ace", "hearts"),
    ("2", "spades"), ("3", "spades"), ("4", "spades"),
    ("5", "spades"), ("6", "spades"), ("7", "spades"),
    ("8", "spades"), ("9", "spades"), ("10", "spades"),
    ("Jack", "spades"), ("Queen", "spades"), ("King", "spades"),
    ("Ace", "spades"),
    ("2", "clubs"), ("3", "clubs"), ("4", "clubs"),
    ("5", "clubs"), ("6", "clubs"), ("7", "clubs"),
    ("8", "clubs"), ("9", "clubs"), ("10", "clubs"),
    ("Jack", "clubs"), ("Queen", "clubs"), ("King", "clubs"),
    ("Ace", "clubs")
]
# ! The above does not feel right. Its clunky and i feel like it would take more memory


class Deck():
    def __init__(self):
        """
        The end of the list is the top, this is a stack
        """
        self.deck = [
            ("2", "diamonds"), ("3", "diamonds"), ("4", "diamonds"),
            ("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"),
            ("8", "diamonds"), ("9", "diamonds"), ("10", "diamonds"),
            ("Jack", "diamonds"), ("Queen", "diamonds"), ("King", "diamonds"),
            ("Ace", "diamonds"), ("2", "hearts"), ("3", "hearts"), ("4", "hearts"),
            ("5", "hearts"), ("6", "hearts"), ("7", "hearts"),
            ("8", "hearts"), ("9", "hearts"), ("10", "hearts"),
            ("Jack", "hearts"), ("Queen", "hearts"), ("King", "hearts"),
            ("Ace", "hearts"), ("2", "spades"), ("3", "spades"), ("4", "spades"),
            ("5", "spades"), ("6", "spades"), ("7", "spades"),
            ("8", "spades"), ("9", "spades"), ("10", "spades"),
            ("Jack", "spades"), ("Queen", "spades"), ("King", "spades"),
            ("Ace", "spades"), ("2", "clubs"), ("3", "clubs"), ("4", "clubs"),
            ("5", "clubs"), ("6", "clubs"), ("7", "clubs"),
            ("8", "clubs"), ("9", "clubs"), ("10", "clubs"),
            ("Jack", "clubs"), ("Queen", "clubs"), ("King", "clubs"),
            ("Ace", "clubs")
        ]
        self.deck_reset = self.deck

        self.size = 52
        self.top = self.deck[0]

    def draw(self):
        if self.size == 0:
            return "All cards have been dealt"
            # ? How would I ask the user if they wanted to reshuffle or play again?
            # ? This would consist of args of a gui or on the command line.
            # ? Would I have to use a while loop and wait for user input?
        self.size -= 1
        top = self.deck.pop()
        if self.deck:
            self.top = self.deck[0]
        else:
            self.top = None
        return top

    def cards_left(self):
        return len(self.deck)

    def shuffle(self):
        if len(self.deck) != 52:
            return "Can't shuffle an unfull deck"
        # to randomize the shuffle with randomness or use an algorithm to insert into?
        # how is a deck shuffled?
        # the deck is layed out and spread into itself on the table
        # the deck is then formed again
        # the deck is split into two with between a 40-60 split
        # then the cards are shuffled
        # repeat twice
        # if the deck is never randomly shuffled first then the outcome will be the same for all instances of deck
        # use overhead random.shuffle to shuffle the deck on the table
        shuffle(self.deck)
        # print(self.deck)

        def split_deck(deck):
            left = deque(deck[:len(deck)//2])
            right = deque(deck[len(deck)//2:])
            new_deck = []
            # the shuffle starts with the bottom of each stack
            # theres no randomness to this should there be?
            while left or right:
                if left:
                    new_deck.append(left.popleft())
                if right:
                    new_deck.append(right.popleft())

            # print(new_deck)
            return new_deck

        self.deck = split_deck(self.deck)

    def reset(self):
        self.size = 52
        self.deck = self.deck_reset
        # if i use pop method to draw a card i cant reset the deck bc there is no value that is to fall back on
        # could I cache the deck? is that possible with python?

        # * Blackjack
        # the deck of cards would be a stack. The head is always the top card and you cannot take from anywhere else.
        # this stack could be an array or a linked list. Depending on memory allocation I would choose the less memory intensive data structure. I would use an array for a deck of cards to access O(1) time to any card. Linked list would take O(n) time to search for a random variable. Although to search for a specific variable would be O(n) in both cases.


        # deal(n) n = amount of players
        # can use an array of arrays to deal cards to each hand. Each player array is indexed in the game array. This holds all cards for players hands
        # hit
        # stay
        # calculate hand
        # dealers hand dependent on calculate hand
        # players hand dependent on calculate hand
        # winner() dependant on dealers hand and player hand values
        # up to 6 players and the dealer so 7
deck = Deck()
deck.shuffle()
deck.shuffle()
deck.shuffle()
# deck_check = []
# print(deck.size)
# print(deck.draw())
# print(deck.size)


class BlackJack():
    def __init__(self):
        # what would I initialize?
        # black hack consists of

        # 1-6 players Class
        # has chip count
        # has actionable events based on the game
        # ? Who has the events the player or the game? or does the game look for the events as arguments?
        # ? Would the player have inputs to tell the dealer and the dealer communicates back based on the game?
        # ? What would be dependent on what? I guess the design is up to me but what is the better option?

        # a dealer Class that inherits player
        # is a player
        # has chip counts as the house
        # deals the cards
        # waits for player input

        # 8 instances of a deck that are all shuffled together

        # a table Class
        # allows a dealer and up to 6 players to sit down
        # a game connot be played unless there is a dealer and at least one player

        # what would be the methods?
        # how many decks do they have?
        # can i shuffle all the decks together?
        pass

    def deal(self, players):  # only can be used by the dealer
        pass
    # deal would need to know how many players are playing and include the dealer
        # inside dependency is hit or stay
        # I need user input for this
        # If the sum of the cards are 22 or above then you bust
        # would this need to be a seperate function for the game?

    def bet():
        pass
    # this action/method would be part of the player subclass

    # would deal have dependecies on methods?
    def check_cards(self):
        # check ths players cards for bust the dealer is also considered a player.
        pass

# the question says to explain how to subclass the data structures to implement black jack.

# * I would need 8 decks, the dealer, the amount of players in the game.
# * The object would only be played until the deck of 8 cards hits the break card.
# * then the decks would be reshuffled all together and the game would be played.
# * players can join and leave after every turn.
# * a turn is when the cards are being dealt
# * a break would be when the cards are not being dealt.
# * the dealer is also a subclass itself it is a player but it is the one dealing the game
# * the object itself can be told to deal because it is electronic but it has to be private.
# * players can only act on playing, leaving, hitting, staying, betting, doubling down
# * There is probably a way to use the object the entire time
# * A player subclass would also need to be implemented with chip_count, actions of betting, hit, stay, and leaving.
# * Actions are only allowed to be used in betting situations.
# * When the dealers is dealing no actions can be used until the dealer comes back to you.
# * then as a player you can split based on your cards, hit, stay, or double down based on your cards.
