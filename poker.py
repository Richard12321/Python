import random

def cardToString(cardindex):
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Bube", "Dame", "König", "Ass"]
    colours = ["Kreuz", "Karo", "Pik", "Herz"]
    return {"number":numbers[cardindex["number"]],"colour":colours[cardindex["colour"]]}

def pull(amount):
    cardpool = []

    for i in range(13):
        for j in range(4):
            cardpool.append({"number": i, "colour": j})

    for i in range(amount):
        rand = random.randrange(0,52)
        cardpool[len(cardpool) - i - 1], cardpool[rand] =\
            cardpool[rand], cardpool[len(cardpool) - i - 1]

    sor = cardpool[len(cardpool)-amount:]
    sor.sort(key=lambda x: x.get("number"))
    return sor

def listNumbers(cards):
    onlyNumbers = []
    for i in cards:
        onlyNumbers.append(i['number'])
    return onlyNumbers

def listCoulours(cards):
    onlyColours = []
    for i in cards:
        onlyColours.append(i['colour'])
    return onlyColours


def royalFlush(cards):
    if straightFlush(cards) and straight(flush(cards)[1])[1]:
        return True
    return False 

def straightFlush(cards):
    if flush(cards)[0]:
        if(straight(flush(cards)[1])[0]):
            return True
    return False 

def poker(cards):
    onlyNumbers = listNumbers(cards)
    for i in range(13):
        if onlyNumbers.count(i) == 4:
            return True
    return False

def fullHouse(cards):
    if pair(cards) >= 1 and triple(cards):
        return True
    return False

def flush(cards):
    coloursOnly = listCoulours(cards)
    fl = []
    for i in range(4):
        if coloursOnly.count(i) >= 5:
            for j in cards:
                if j["colour"] == i:
                    fl.append(j) 
            return (True, fl)
    return (False, fl)


def straight(cards):
    followings = 1
    royal = False
    for i in range(len(cards)-1):
        if cards[i+1]["number"] - cards[i]["number"] == 0:
            continue
        if cards[i+1]["number"] - cards[i]["number"] == 1:
            followings += 1
            if cards[i+1]["number"] == 12:
                royal = True
            if followings == 5:
                return (True, royal)
            continue
        followings = 1
    return (False, royal)

def triple(cards):
    onlyNumbers = listNumbers(cards)
    for i in range(13):
        if onlyNumbers.count(i) == 3:
            return True
    return False

def pair(cards):
    pairs = 0
    onlyNumbers = listNumbers(cards)
    for i in range(13):
        if onlyNumbers.count(i) == 2:
            pairs += 1
    return pairs

def hand(cards):
    if royalFlush(cards):
        return "royalFlush"
    elif straightFlush(cards):
        return "straightFlush"
    elif poker(cards):
        return "poker"
    elif fullHouse(cards):
        return "fullHouse"
    elif flush(cards)[0]:
        return "flush"
    elif straight(cards)[0]:
        return "straight"
    elif triple(cards):
        return "triple"
    elif pair(cards) == 2:
        return "twoPair"
    elif pair(cards) == 1:
        return "pair"
    else: 
        return "high"

def stats(pulls, cardsPerPull):
    stat = {"royalFlush": 0, "straightFlush": 0, "poker": 0, "fullHouse": 0,\
            "flush": 0,"straight": 0, "triple": 0, "twoPair": 0, "pair": 0,\
            "high": 0}
    for i in range(pulls):
        stat[hand(pull(cardsPerPull))] += 1
    statPercent = {"royalFlush": (stat["royalFlush"]/pulls)*100, \
            "straightFlush": (stat["straightFlush"]/pulls)*100, \
            "poker": (stat["poker"]/pulls)*100, \
            "fullHouse": (stat["fullHouse"]/pulls)*100, \
            "flush": (stat["flush"]/pulls)*100,\
            "straight": (stat["straight"]/pulls)*100,\
            "triple": (stat["triple"]/pulls)*100,\
            "twoPair": (stat["twoPair"]/pulls)*100,\
            "pair": (stat["pair"]/pulls)*100, "high": (stat["high"]/pulls)*100}
    return (stat, statPercent)

def main():
    pulls = int(input("Ziehungen?"))
    cardsPerPull = int(input("Karten pro Ziehungen?"))
    statperc = stats(pulls,cardsPerPull)[1]
    statabs = stats(pulls,cardsPerPull)[0]
    breakpoint()
    print("Number of drawn cards:     \t", pulls)
    print("Highest-Card:              \t", str(round(statperc["high"], 4)), " % \t", statabs["high"])
    print("One-Pair:                  \t", str(round(statperc["pair"], 4)), " %  \t", statabs["pair"])
    print("Two-Pair:                  \t", str(round(statperc["twoPair"], 4)), " %  \t", statabs["twoPair"])
    print("Triple:                    \t", str(round(statperc["triple"], 4)), " %  \t", statabs["triple"])
    print("Straight:                  \t", str(round(statperc["straight"], 4)), " %  \t", statabs["straight"])
    print("Flush:                     \t", str(round(statperc["flush"], 4)), " %  \t", statabs["flush"])
    print("Full-House:                \t", str(round(statperc["fullHouse"], 4)), " %  \t", statabs["fullHouse"])
    print("Four-Of-A-Kind:            \t", str(round(statperc["poker"], 4)), " %  \t", statabs["poker"])
    print("Straight-Flush:            \t", str(round(statperc["straightFlush"], 4)), " %  \t", statabs["straightFlush"])
    print("Royal-Flush:               \t", str(round(statperc["royalFlush"], 4)), " %  \t", statabs["royalFlush"])
    #print(cardToString(pull(5)[0]))

if __name__ == "__main__":
    main()