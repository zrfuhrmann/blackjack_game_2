import random
from card_class import Card
from deck_class import Deck
from hand_class import Hand


def get_correct_input(target_list, user_input, change_to_int=0):
    while user_input not in target_list:
        user_input = input("Please enter proper input ==>> ")

    if change_to_int == 1:
        return int(user_input)
    else:
        return user_input


def get_user_bet(u_money):
    str_list = []
    for i in range(1, u_money + 1):
        str_list.append(str(i))

    print("You have $", u_money, sep="")
    bet = input("Please enter your bet in whole USD (You must bet some amount) ==>> ")
    return get_correct_input(str_list, bet, 1)


def get_cpu_bet(cpu_money):
    return random.randint(1, cpu_money)


def get_pot(u_bet, u_money, cpu_bet, cpu_money):
    return (u_bet + cpu_bet), (u_money - u_bet), (cpu_money - cpu_bet)


"""The game starts here"""
play_again = "Yes"
while play_again == "Yes":
    user_money = 10000
    cpu1_money = 10000
    while user_money > 0 and cpu1_money > 0:
        user_bet = get_user_bet(user_money)
        cpu1_bet = get_cpu_bet(cpu1_money)
        print("The computer bet $", cpu1_bet, sep="")

        pot, user_money, cpu1_money = get_pot(user_bet, user_money, cpu1_bet, cpu1_money)

        new_deck = Deck
        new_deck.shuffle()
        user_hand = Hand()
        cpu1_hand = Hand()

        user_hand.add_to_hand(new_deck.deal())
        cpu1_hand.add_to_hand(new_deck.deal())
        user_hand.add_to_hand(new_deck.deal())
        cpu1_hand.add_to_hand(new_deck.deal())

        user_hand.print_hand()

    play_again = input("Would you like to play again? (Enter 'Yes' or 'No') ==>> ")
    play_again = get_correct_input(["Yes", "No"], play_again)  # comment added
    print("Hello World")
