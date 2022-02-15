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
