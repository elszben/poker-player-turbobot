import random

odds = [
    0.995,
    1.37,
    20,
    46.3,
    254,
    508,
    693,
    4165,
    72192
    ]

# {fold, call, raise}
bet_chance = [
    [100, 0, 0, 0],
    [80, 20, 0, 0],
    [30, 30, 40, 100],
    [10, 40, 50, 100],
    [5, 45, 50, 200],
    [0, 50, 50, 200],
    [0, 30, 70, 300],
    [0, 20, 80, 1000],
    [0, 0, 100, 1000]
    ]

card_value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
    }

max_sum=69

def get_bet(current_money, result, cards, rank):
    card_sum = 0
    for card in cards:
        card_sum += card_value[card["rank"]]

    max_raise = card_sum * bet_chance[rank][3] // max_sum

    r = random.randint(0, 100)
    r1 = random.randint(current_money/2, current_money)

    chance = bet_chance[rank]
    if r<=chance[0]:
        return 0
    elif r<=(chance[0] + chance[1]):
        return result if result<=max_raise else 0
    else:
        return max_raise * r1 // 1000

if __name__=="__main__":
    print get_bet(1000, 200, [{"rank":"8","suit":"hearts"},
                              {"rank":"8","suit":"spades"},
                              {"rank":"J","suit":"diamonds"},
                              {"rank":"J","suit":"clubs"},
                              {"rank":"Q","suit":"diamonds"}], 2)
    print get_bet(1000, 200, [{"rank":"3","suit":"clubs"},
                              {"rank":"4","suit":"spades"},
                              {"rank":"7","suit":"spades"},
                              {"rank":"9","suit":"clubs"},
                              {"rank":"Q","suit":"clubs"}], 0)
    print get_bet(1000, 200, [{"rank":"6","suit":"diamonds"},
                              {"rank":"8","suit":"diamonds"},
                              {"rank":"10","suit":"diamonds"},
                              {"rank":"J","suit":"diamonds"},
                              {"rank":"A","suit":"diamonds"}], 5)
