# CTCI 7.1 Deck Of Cards

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
deck = [("2", "Diamonds"), ("3", "Diamonds"), ("4", "Diamonds"),
        ("5", "Diamonds"), ("6", "Diamonds"), ("7", "Diamonds"),
        ("8", "Diamonds"), ("9", "Diamonds"), ("10", "Diamonds"),
        ("Jack", "Diamonds"), ("Queen", "Diamonds"), ("King", "Diamonds"),
        ("Ace", "Diamonds")]

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
