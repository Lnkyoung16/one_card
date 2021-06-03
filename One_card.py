import random

def card_deck_generator():
    temporary = []
    while len(temporary) != 1:
        card_number = random.randint(1, 12)
        card_shape = random.randint(0, 3)
        if card_shape == 0:
            card_shape = "♠"
        elif card_shape == 1:
            card_shape = "♣"
        elif card_shape == 2:
            card_shape = "♥"
        else:
            card_shape = "♦"
        if card_number == 1:
            card_number = "A"
        elif card_number == 10:
            card_number = "J"
        elif card_number == 11:
            card_number = "Q"
        elif card_number == 12:
            card_number = "K"
        card = card_shape + str(card_number)
        overlap = check_overlap(card)
        if overlap != 0:
            return card