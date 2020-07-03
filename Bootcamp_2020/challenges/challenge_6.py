"""
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','jack','queen', 'king']
"""
deck = dict()
suits = ['diamonds', 'hearts', 'spades', 'clubs']
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
for card_suits in suits:
    deck[card_suits] = rank
print(deck)
