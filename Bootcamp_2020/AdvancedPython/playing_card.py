class Card(object):
    """
        Attributes
        ----------
        val: card number
        suit: graphic symbols or 'pips'
    """

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit.lower()[0]
        self.values = {1: 'Ace', 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
                       8: 8,
                       9: 9, 10: 10, 11: 'Jack', 12: 'Queen',
                       13: 'King'}
        self.pips = {'c': 'clubs', 'h': 'hearts', 's': 'spades',
                     'd': 'diamonds'}

    def get_value(self):
        return self.val

    def get_suit(self):
        return self.suit

    def __str__(self):
        if self.val > 13 or not self.val >= 1 or\
                self.suit not in 'chds':
            return 'There is no card'
        else:
            my_card = str(self.values[self.val].upper()) + ' of ' + \
                  str(self.pips[self.suit].upper())
            return my_card


my_cards = Card(13, 'd')
print(my_cards)
