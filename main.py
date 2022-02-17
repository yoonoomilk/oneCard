import random
import time
import os

spade = """
 ㅡㅡㅡㅡㅡㅡ
|            |
|     ■■     |
|    ■■■■    |
|  ■■■■■■■■  |
| ■■■■  ■■■■ |
| ■■  ■■  ■■ |
|     ■■     |
|    ■■■■    |
 ㅡㅡㅡㅡㅡㅡ
"""[1:-1]
clover = """
 ㅡㅡㅡㅡㅡㅡ
|            |
|     ■■     |
|    ■■■■    |
|  ■■ ■■ ■■  |
| ■■■■■■■■■■ |
|  ■■ ■■ ■■  |
|    ■■■■    |
|   ■■■■■■   |
 ㅡㅡㅡㅡㅡㅡ
"""[1:-1]
heart = """
 ㅡㅡㅡㅡㅡㅡ
|            |
|  ■      ■  |
| ■■■■  ■■■■ |
| ■■■■■■■■■■ |
|  ■■■■■■■■  |
|   ■■■■■■   |
|    ■■■■    |
|     ■■     |
 ㅡㅡㅡㅡㅡㅡ
"""[1:-1]
diamond = """
 ㅡㅡㅡㅡㅡㅡ
|            |
|     ■■     |
|    ■■■■    |
|   ■■■■■■   |
|  ■■■■■■■■  |
|   ■■■■■■   |
|    ■■■■    |
|     ■■     |
 ㅡㅡㅡㅡㅡㅡ
"""[1:-1]
joker = """
 ㅡㅡㅡㅡㅡㅡ
|            |
|            |
|  ■      ■  |
|     ■■     |
|  ■      ■  |
|  ■■    ■■  |
|   ■    ■   |
|    ■■■■    |
 ㅡㅡㅡㅡㅡㅡ
"""[1:-1]

def show(temp):
    (shape_temp, num) = temp
    if shape_temp == "♠":
        shape = spade
    elif shape_temp == "♣":
        shape = clover
    elif shape_temp == "♥":
        shape = heart
    elif shape_temp == "♦":
        shape = diamond
    else:
        shape = joker
    if len(num) == 1:
        num = " " + num
    elif num == "colored":
        num = " ♦"
    elif num == "black":
        num = " ♠"
    shape = list(shape)
    shape[18:20] = num
    return "".join(shape)

def isNumber(n):
  try:
    int(n)
    return True
  except:
    return False

# 가능한 카드 리스트를 반환
def getAvailable(hand, last_card, is_attack):
    available = []
    if not is_attack and last_card[0] == "Joker":
        available.extend(hand)
        return available

    for card in hand:
        if card[0] == "Joker":
            available.append(card)

        elif (card[0] != last_card[0] and card[1] != last_card[1]):
            continue

        elif is_attack:
            if get_damage(card) >= get_damage(last_card) or card[1] == "3":
                available.append(card)
        else:
            available.append(card)

    return available


is_attack = False
damage = 1


def is_attack_card(card):
    return card[0] == "Joker" or card[1] in ["A", "2"]

def is_defense_card(card):
    return card[1] == "3"

def is_effect_card(card):
    return card[1] in ["J", "K"]

damage_map = {
    "colored": 7,
    "black": 5,
    "A": 3,
    "2": 2,
    "3": 0
}


def get_damage(card):
    global damage_map
    return damage_map.get(card[1], 0)


def draw(hand):
    global put, deck

    hand.append(deck.pop())

    if len(deck) == 0:
        print_message("카드를 다시 섞습니다!")
        last_card = put.pop()
        random.shuffle(put)
        put, deck = deck, put
        put.append(last_card)


def card_str(card):
    return f"[{card[0]}{card[1]}]"


def hand_str(hand):
    return " ".join(map(card_str, hand))

def canwin(hand):
    for i in hand:
        if i[1] in ["K", "J"]:
            hand.remove(i)
    return len(hand) <= 1

message_count = 0
messages = []
log = []


def print_message(message):
    global put, deck, player, is_attack, messages, message_count
    os.system("cls")

    output = []
    output.append(f"마지막으로 놓은 카드\n{show(put[-1])}")
    output.append(f"현재 있는 카드     \t{hand_str(player)}")
    output.append(f"놓을 수 있는 카드  \t{hand_str(getAvailable(player, put[-1], is_attack))}")
    output.append("-" * 30)

    message_count += 1
    messages.append(message)
    log.append(message)
    if len(messages) == 14:
        messages.pop(0)
    for i, m in enumerate(messages):
        output.append(f"[{message_count - len(messages) + i + 1:>3}] {m}")
    output.append("-" * 30)

    print("\n".join(output))


def turn(hand, isComputer):

    # 전역 변수 접근
    global put, deck, is_attack, damage
    # 이름 정하기
    if isComputer:
        name = "컴퓨터"
    else:
        name = "플레이어"

    # 차례
    print_message(f"{name}의 차례입니다.")
    flag = 0

    # ----------- 낼 수 있는 카드 고르기 ---------------
    available = getAvailable(hand, put[-1], is_attack)

    # ----------- 카드 고르기 ---------------------
    is_available = len(available) > 0
    if is_available:
        if isComputer:
            global player
            #지금 J, K로 이길 수 있는지 확인
            if canwin(hand):
                temp = []
                for i in available:
                    if is_effect_card(i):
                        temp.append(i)
                if temp:
                    selected = random.choice(temp)
                else:
                    selected = random.choice(available)
            #상대 패가 적은지 확인
            elif len(player) < 3:
                temp = []
                for i in available:
                    if is_attack_card(i):
                        temp.append(i)
                #만약 공격 카드가 있다면 사용
                if temp:
                    selected = random.choice(temp)
                else:
                    selected = random.choice(available)
            #상대 패가 많고 공격을 했다면
            elif is_attack:
                temp = []
                for i in available:
                    if is_defense_card(i):
                        temp.append(i)
                #만약 방어 카드가 있다면
                if temp:
                    selected = random.choice(temp)
                else:
                    selected = random.choice(available)
            else:
                selected = random.choice(available)
        else:
            i = 0
            while True:
                i = input("몇 번째 카드를 내시겠습니까? ")
                if isNumber(i):
                    i = int(i)
                    if -1 < i-1 < len(available):
                        selected = available[i-1]
                        break
                print_message("범위를 벗어났습니다.")
        hand.remove(selected)
        put.append(selected)

        if is_attack_card(selected):
            if not is_attack:
                damage = get_damage(selected)
            else:
                damage += get_damage(selected)
            is_attack = True
        elif is_defense_card(selected):
            damage = 1
        elif is_effect_card(selected):
            flag = 1

        print_message(f"{name}가 {selected}를 냈습니다. (남은카드 {len(hand)}장)")

    # ------------ 카드 먹기 -----------------------
    else:
        print_message(f"{name}가 낼 수 있는 카드가 없어 {damage}장 먹습니다.")
        if not isComputer:
            input("계속 하려면 엔터를 누르세요.")
        is_attack = False
        for i in range(damage):
            draw(hand)
        damage = 1
    if len(hand) == 0:
        print_message(f"{name}가 이겼습니다!")
        return True
    elif flag:
        turn(hand, isComputer)
    else:
        return False


deck = []

# num과 shape 정의
shapes = "♠♣♥♦"
nums = []
for i in range(2, 11):
    nums.append(str(i))
for c in "JQKA":
    nums.append(c)

# 덱 만들기
for shape in shapes:
    for num in nums:
        deck.append((shape, num))

deck.append(("Joker", "black"))
deck.append(("Joker", "colored"))
random.shuffle(deck)

# 플레이어에게 카드 나누기

player = []
computer = []

for i in range(7):
    player.append(deck.pop())
    computer.append(deck.pop())

# 낸 카드에 하나 올려놓기
put = []
put.append(deck.pop())

# 게임 시작
while True:

    if turn(player, False):
        break

    if turn(computer, True):
        break

os.makedirs("C:/Users/Public/Documents/milk/onecard", exist_ok=True)
os.chdir("C:/Users/Public/Documents/milk/onecard")
log_name = str(int(time.time()*1000000))+".txt"
f = open(log_name, "w", encoding="utf-8")
for i in log:
    f.write(i)
    f.write("\n")
f.close()
input(f"로그가 {log_name}에 저장되었습니다.")
