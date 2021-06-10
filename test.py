# list = ['a', 'b', 'c', 'd', 'e', 'f']
#
# print(list[1:])

for i in range(0,10):
    print(i)

import time
import random

random_number = random.randint(0,9)
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

card = "♣4"
card[1:]