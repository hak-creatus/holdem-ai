import random


class Card(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        value_name = ""
        if self.value == 0:
            value_name = "Two"
        elif self.value == 1:
            value_name = "Three"
        elif self.value == 2:
            value_name = "Four"
        elif self.value == 3:
            value_name = "Five"
        elif self.value == 4:
            value_name = "Six"
        elif self.value == 5:
            value_name = "Seven"
        elif self.value == 6:
            value_name = "Eight"
        elif self.value == 7:
            value_name = "Nine"
        elif self.value == 8:
            value_name = "Ten"
        elif self.value == 9:
            value_name = "Ace"

        return value_name


class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(10))
        [[self.append(Card(i)) for j in suits] for i in values]

    def shuffle(self):
        random.shuffle(self)
        print("Deck shuffled")

    def deal(self):
        return self.pop(0)


deck = StandardDeck()
