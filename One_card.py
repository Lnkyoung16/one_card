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
        self.attack_finish = 0


    def check_overlap(self, card, list):
        total_list = self.computer_card_deck + self.player_card_deck + list
        duplicated_card = 0
        for i in range(0, len(total_list)):
            if card == total_list[i]:
                duplicated_card = duplicated_card + 1
        return duplicated_card

    def card_deck_generator(self):
        temporary = []
        card_shape = "0"
        card_number = 0
        for i in range(1,14):
            for j in range(0,4):
                if j == 0:
                    card_shape = "♠"
                elif j == 1:
                    card_shape = "♣"
                elif j == 2:
                    card_shape = "♥"
                else:
                    card_shape = "♦"
                if i == 1:
                    card_number = "A"
                elif i == 11:
                    card_number = "J"
                elif i == 12:
                    card_number = "Q"
                elif i == 13:
                    card_number = "K"
                else:
                    card_number = str(i)
                card = card_shape + str(card_number)
                temporary.append(card)
        random.shuffle(temporary)
        self.unused_card_deck = temporary


    def card_shape_validator(self, card):
        if card[:1] == self.top_card_of_deck[:1]:
            return 0

    def card_number_validator(self, card):
        if card[1:] == self.top_card_of_deck[1:]:
            return 0

    def attack_card_validator(self, card):
        if card[1:] == 'A' or card[1:] == '2' or card [1:] == '3':
            return 0

    def attack_validator(self, card):
        if card[1:] == 'A':
            self.attack_check = 1
            print(self.attack_check)

    def computer_card_release(self):
        card_candidate = []
        for i in range(0, len(self.computer_card_deck)):
            if self.card_shape_validator(self.computer_card_deck[i]) == 0 or self.card_number_validator(self.computer_card_deck[i]) == 0:
                card_candidate.append(self.computer_card_deck[i])
        if len(card_candidate) == 0:
            self.card_distributer(1, 1)
            print("컴퓨터가 카드를 한장 먹었습니다.")
        else:
            card = card_candidate[random.randint(0, len(card_candidate) - 1)]
            self.computer_card_deck.remove(card)
            self.top_card_of_deck = card
            self.attack_validator(card)
            print("컴퓨터는", card, "을(를) 냈습니다.")

    def computer_card_release_attack(self):
        card_candidate = []
        for i in range(0, len(self.computer_card_deck)):
            if self.card_shape_validator(self.computer_card_deck[i]) == 0 or self.attack_card_validator(self.computer_card_deck[i]) == 0:
                card_candidate.append(self.computer_card_deck[i])
        if len(card_candidate) == 0:
            self.attack_finish = 1
            print("컴퓨터는 카드를 내지 못했습니다.")
        else:
            card = card_candidate[random.randint(0, len(card_candidate)-1)]
            self.computer_card_deck.remove(card)
            self.top_card_of_deck = card
            self.used_card_deck_attack.append(card)
            print("컴퓨터는", card, "을(를) 냈습니다.")

    def card_distributer(self, number, sequence):
        if sequence == 0:
            for i in range(0, number):
                self.player_card_deck.append(self.unused_card_deck[0])
                self.unused_card_deck = self.unused_card_deck[1:]
        else:
            for i in range(0, number):
                self.computer_card_deck.append(self.unused_card_deck[0])
                self.unused_card_deck = self.unused_card_deck[1:]

    def card_gain_calculator(self):
        self.number_gain_card = 0
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
        while True:
            sequence_card = int(input("몇번째 카드를 내시겠습니까? 카드를 추가로 얻으시려면 0을 입력해주세요."))
            if sequence_card == 0:
                self.card_distributer(1, 0)
                print("카드를 한장 먹었습니다.")
                break
            else:
                sequence_card = sequence_card - 1
                card = self.player_card_deck[sequence_card]
                if self.card_number_validator(card) == 0 or self.card_shape_validator(card) == 0:
                    self.top_card_of_deck = card
                    self.player_card_deck.remove(card)
                    self.attack_validator(card)
                    break
                else:
                    print("올바른 카드를 내주세요. 모양 또는 숫자가 일치해야합니다.")


    def game_attack(self):
        print(self.player_card_deck)
        while True:
            sequence_card = int(input("몇번째 카드를 내시겠습니까? 내실 카드가 없으시다면 0을 입력해주세요."))
            if sequence_card == 0:
                self.attack_finish = 0
                break
            else:
                sequence_card = sequence_card - 1
                card = self.player_card_deck[sequence_card]
                if self.attack_card_validator(card) == 0 or self.card_shape_validator(card) == 0:
                    self.top_card_of_deck = card
                    self.player_card_deck.remove(card)
                    self.used_card_deck_attack.append(card)
                    break
                else:
                    print("올바른 카드를 내주세요. 모양이 일치해야하며 숫자는 A, 2. 3만 가능합니다.")

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
            return 1
        else:
            print("플레이어 승")
            print(time_end, "초가 걸렸습니다.")
            return 0

    def game_start(self):
        self.sequence = self.call_one_card()
        self.card_deck_generator()
        self.card_distributer(7, 0)
        self.card_distributer(7, 1)
        self.top_card_of_deck = self.unused_card_deck[0]
        self.unused_card_deck = self.unused_card_deck[1:]
        print(self.top_card_of_deck, "은(는) 맨 위의 카드입니다.")
        while True:
            print(self.attack_check)
            if self.sequence == 0:
                if self.attack_check == 0:
                    print("플레이어의 차례입니다.")
                    self.game_normal()
                    self.sequence = 1
                    print(self.top_card_of_deck, "은(는) 맨 위의 카드입니다.")
                else:
                    print("플레이어의 차례입니다.")
                    self.game_attack()
                    self.sequence = 1
                    print(self.top_card_of_deck, "은(는) 맨 위의 카드입니다.")
            else:
                if self.attack_check == 0:
                    print("컴퓨터의 차례입니다.")
                    self.computer_card_release()
                    self.sequence = 0
                    print(self.top_card_of_deck, "은(는) 맨 위의 카드입니다.")
                else:
                    print("컴퓨터의 차례입니다.")
                    self.computer_card_release_attack()
                    self.sequence = 0
                    print(self.top_card_of_deck, "은(는) 맨 위의 카드입니다.")
            # if self.attack_finish == 1:
            #     self.card_gain_calculator()
            #     self.card_distributer(self.number_gain_card, 1)
            #     self.attack_check = 0
            # elif self.attack_finish == 0:
            #     self.card_gain_calculator()
            #     # if len(self.unused_card_deck) < self.number_gain_card:
            #     #     self.card_deck_generator()
            #     self.card_distributer(self.number_gain_card, 0)
            #     self.attack_check = 0





one_card().game_start()