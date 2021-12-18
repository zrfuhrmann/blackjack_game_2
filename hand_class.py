from card_class import Card


class Hand:
    def __init__(self):
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = 0
        for card in self.hand:
            value += card.get_card_value()

        return value

    def print_hand(self):
        print("Your hand consists of")
        for i in self.hand:
            print(i.get_card_name())

        print("Hand value:", self.get_hand_value())
