from card_class import Card
import random


class Deck:
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self):
        self.cards = []
        for i in Deck.suits:
            for j in range(len(Deck.names)):
                self.cards.append(Card(("a(n) " + Deck.names[j] + " of " + i), Deck.values[j]))

    def deal(self):
        return self.cards.pop(0)

    def shuffle(self):
        for i in range(10):
            for j in range(52):
                self.cards.insert(random.randint(0, 51), self.cards.pop(j))

    def view_card(self, index):
        print(self.cards[index].get_card_name(), "value", self.cards[index].get_card_value())
