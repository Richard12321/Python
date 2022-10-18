import random

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Bube", "Dame", "König", "Ass"]
colours = ["Kreuz", "Karo", "Pik", "Herz"]

def card(cardindex):
    return (numbers[cardindex[0]],colours[cardindex[1]])

def pull(amount):
    cardpool = []

    for i in range(13):
        for j in range(4):
            cardpool.append((i,j))

    for i in range(amount):
        rand = random.randrange(0,52)
        cardpool[len(cardpool) - i - 1], cardpool[rand] = cardpool[rand], cardpool[len(cardpool) - i - 1]

    return cardpool[len(cardpool)-amount:]

for b in pull(5):
    print(card(b))