import random
import array


class Card:
    """An individual card"""
    def __init__(self):
        self.Values = array.array('i', [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
        self.allCards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['♥', '♦', '♣', '♠']
        self.face_value = random.randint(0, 12)
        self.string_value = self.allCards[self.face_value] + self.suits[random.randint(0, 3)]
        self.count_value = self.Values[self.face_value]

    def get_string_value(self):
        return self.string_value

    def get_count_value(self):
        return self.count_value
