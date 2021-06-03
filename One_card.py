import random
import time

player_card_deck = []
computer_card_deck = []
unused_card_deck = []
top_card_of_deck = 0
used_card_deck_attack = []
sequence = 0
attack_check = 0
number_gain_card = 0


def check_overlap(card):
    total_list = computer_card_deck + player_card_deck + unused_card_deck
    for i in range(0, len(total_list)):
        if card == total_list[i]:
            return 0

def card_deck_generator():
    temporary = []
    while len(temporary) != 1:
        card_number_t = random.randint(1, 12)
        card_shape_t = random.randint(0, 3)
        if card_shape_t == 0:
            card_shape = "♠"
        elif card_shape_t == 1:
            card_shape = "♣"
        elif card_shape_t == 2:
            card_shape = "♥"
        else:
            card_shape = "♦"
        if card_number_t == 1:
            card_number = "A"
        elif card_number_t == 10:
            card_number = "J"
        elif card_number_t == 11:
            card_number = "Q"
        elif card_number_t == 12:
            card_number = "K"
        card = card_shape + str(card_number)
        overlap = check_overlap(card)
        if overlap != 0:
            return card

def card_shape_validator(card):
    if card[:1] == top_card_of_deck[:1]:
        return 0

def card_number_validator(card):
    if card[1:] == top_card_of_deck[1:]:
        return 0

def attack_card_validator(card):
    if card[:1] == 'A' or card[:1] == '2' or card [:1] == '3':
        return 0

def computer_card_release():
    card_candidate = []
    for i in range(0, len(computer_card_deck)):
        if card_shape_validator(computer_card_deck[i]) == 0 or card_number_validator(computer_card_deck[i]) == 0:
            card_candidate.append(i)
    card = card_candidate[random.randint(0,len(card_candidate))]
    return card

def computer_card_release_attack():
    card_candidate = []
    for i in range(0, len(computer_card_deck)):
        if card_shape_validator(computer_card_deck[i]) == 0 or attack_card_validator(computer_card_deck[i]) == 0:
            card_candidate.append(i)
    card = card_candidate[random.randint(0, len(card_candidate))]
    return card

def card_distributer(number, unused_card_deck):

    if sequence == 0:
        for i in range(0, number):
            player_card_deck.append(unused_card_deck[1])
            unused_card_deck = unused_card_deck[1:]
    else:
        for i in range(0, number):

            computer_card_deck.append(unused_card_deck[1])

def card_gain_calculator():
    for i in range(0, len(used_card_deck_attack)):
        card = used_card_deck_attack[i]
        card_shape = card[:1]
        card_number = card[1:]
        if card_number == 'A':
            if card_shape == '♠':
                number_gain_card = number_gain_card + 4
            else:
                number_gain_card = number_gain_card + 3
        elif card_number == '2':
            number_gain_card = number_gain_card + 2
        elif card_number == '3':
            number_gain_card = number_gain_card + 1

def game_normal():
    print(player_card_deck)
    sequence_card = int(input("몇번째 카드를 내시겠습니까?"))
    sequence_card = sequence_card - 1
    card = player_card_deck[sequence_card]
    while True:
        if card_number_validator(card) == 0 and card_shape_validator(card) == 0:
            break
        else:
            print("올바른 카드를 내주세요. 모양 또는 숫자가 일치해야합니다.")


def game_attack():
    print(player_card_deck)
    sequence_card = int(input("몇번째 카드를 내시겠습니까?"))
    sequence_card = sequence_card - 1
    card = player_card_deck[sequence_card]
    while True:
        if card_number_validator(card) == 0 and card_shape_validator(card) == 0:
            break
        else:
            print("올바른 카드를 내주세요. 모양이 일치해야하며 숫자는 A, 2. 3만 가능합니다.")

def card_shape_change():
    card_shape = int(input("어느 모양으로 바꾸시겠습니까? 1:♠, 2:♣, 3:♥, 4:♦"))
    card_shape = card_shape - 1
    if card_shape == 0:
        card_shape = "♠"
    elif card_shape == 1:
        card_shape = "♣"
    elif card_shape == 2:
        card_shape = "♥"
    else:
        card_shape = "♦"

def call_one_card():
    random_number = random.randint(0,9)
    random_time = random.randint(1, 4)
    print("원카드 외치기 - 숫자 외치기")
    print(random_number)
    input_number = int(input("위에 뜬 숫자를", random_time, "내에 빠르게 입력하세요."))
    time.sleep(random_time)
    if input_number == random_number:



# if top_card_of_deck[:1] == 'A':
#     attack_check = 1