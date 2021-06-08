import random
import time

class one_card:
    def __init__(self):
        self.player_card_deck = []
        self.computer_card_deck = []
        self.unused_card_deck = []
        self.top_card_of_deck = 0
        self.used_card_deck_attack = []
        self.sequence = 0
        self.attack_check = 0
        self.number_gain_card = 0


    def check_overlap(self, card, list):
        total_list = self.computer_card_deck + self.player_card_deck + list
        print("computer_card_deck: ", self.computer_card_deck, "player_card_deck: ", self.player_card_deck , "list : ", list)
        duplicated_card = 0
        for i in range(0, len(total_list)):
            if card == total_list[i]:
                duplicated_card = duplicated_card + 1
        return duplicated_card

    def card_deck_generator(self):
        temporary = []
        number_of_card = 52 - len(self.player_card_deck) - len(self.computer_card_deck)
        card_shape = "0"
        card_number = 0
        print("number_of_card:", number_of_card)
        while len(temporary) != number_of_card:
            print("card_number:", card_number, "card_shape_t:", card_shape_t)
            if card_shape_t == 0:
                card_shape = "♠"
            elif card_shape_t == 1:
                card_shape = "♣"
            elif card_shape_t == 2:
                card_shape = "♥"
            else:
                card_shape = "♦"
            print("card_shape:", card_shape)
            if card_number == 1:
                card_number = "A"
            elif card_number == 10:
                card_number = "J"
            elif card_number == 11:
                card_number = "Q"
            elif card_number == 12:
                card_number = "K"
            print("card_number:", card_number)
            card = card_shape + str(card_number)
            overlap = self.check_overlap(card, temporary)
            print("overlap:", overlap)
            print("card:", card)
            if overlap == 0:
                temporary.append(card)
                print("temporary:", temporary)
        self.unused_card_deck = temporary

    def card_shape_validator(self, card):
        if card[:1] == self.top_card_of_deck[:1]:
            return 0

    def card_number_validator(self, card):
        if card[1:] == self.top_card_of_deck[1:]:
            return 0

    def attack_card_validator(self, card):
        if card[:1] == 'A' or card[:1] == '2' or card [:1] == '3':
            return 0

    def computer_card_release(self):
        card_candidate = []
        for i in range(0, len(self.computer_card_deck)):
            if self.card_shape_validator(self.computer_card_deck[i]) == 0 or self.card_number_validator(self.computer_card_deck[i]) == 0:
                card_candidate.append(i)
        card = card_candidate[random.randint(0,len(card_candidate))]
        self.computer_card_deck = self.computer_card_deck.remove(card)
        return card

    def computer_card_release_attack(self):
        card_candidate = []
        for i in range(0, len(self.computer_card_deck)):
            if self.card_shape_validator(self.computer_card_deck[i]) == 0 or self.attack_card_validator(self.computer_card_deck[i]) == 0:
                card_candidate.append(i)
        card = card_candidate[random.randint(0, len(card_candidate))]
        self.computer_card_deck = self.computer_card_deck.remove(card)
        return card

    def card_distributer(self, number):
        if self.sequence == 0:
            for i in range(0, number):
                self.player_card_deck.append(self.unused_card_deck[1])
                self.unused_card_deck = self.unused_card_deck[1:]
        else:
            for i in range(0, number):
                self.computer_card_deck.append(self.unused_card_deck[1])
                self.unused_card_deck = self.unused_card_deck[1:]

    def card_gain_calculator(self):
        for i in range(0, len(self.used_card_deck_attack)):
            card = self.used_card_deck_attack[i]
            card_shape = card[:1]
            card_number = card[1:]
            if card_number == 'A':
                if card_shape == '♠':
                    self.number_gain_card = self.number_gain_card + 4
                else:
                    self.number_gain_card = self.number_gain_card + 3
            elif card_number == '2':
                self.number_gain_card = self.number_gain_card + 2
            elif card_number == '3':
                self.number_gain_card = self.number_gain_card + 1

    def game_normal(self):
        print(self.player_card_deck)
        sequence_card = int(input("몇번째 카드를 내시겠습니까?"))
        sequence_card = sequence_card - 1
        card = self.player_card_deck[sequence_card]
        self.player_card_deck = self.player_card_deck.pop(sequence_card)
        while True:
            if self.card_number_validator(card) == 0 and self.card_shape_validator(card) == 0:
                break
            else:
                print("올바른 카드를 내주세요. 모양 또는 숫자가 일치해야합니다.")


    def game_attack(self):
        print(self.player_card_deck)
        sequence_card = int(input("몇번째 카드를 내시겠습니까?"))
        sequence_card = sequence_card - 1
        card = self.player_card_deck[sequence_card]
        self.player_card_deck = self.player_card_deck.pop(sequence_card)
        while True:
            if self.card_number_validator(card) == 0 and self.card_shape_validator(card) == 0:
                break
            else:
                print("올바른 카드를 내주세요. 모양이 일치해야하며 숫자는 A, 2. 3만 가능합니다.")

    def card_shape_change(self):
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

    def call_one_card(self):
        random_number = random.randint(0, 9)
        random_time = random.randint(1, 4)
        print("원카드 외치기 - 숫자 외치기")
        print(random_number, "을(를)", random_time, "초 내에 빠르게 입력하세요.")
        time_start = time.time()
        while True:
            input_number = int(input("숫자 입력:"))
            if input_number == random_number:
                break
            else:
                print("숫자를 정확하게 입력해주세요.")
        time_end = time.time() - time_start
        if time_end > random_time:
            print("컴퓨터 승")
            print(time_end, "초가 걸렸습니다.")
        else:
            print("플레이어 승")
            print(time_end, "초가 걸렸습니다.")

    def game_start(self):
        self.card_deck_generator()
        print(self.unused_card_deck)
        self.card_distributer(7)
        self.sequence = 1
        self.card_distributer(7)
        print(self.computer_card_deck)
        print(self.player_card_deck)
        print(self.unused_card_deck)


one_card().game_start()