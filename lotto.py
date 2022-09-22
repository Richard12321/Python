import random

def lottoziehung():
    zahlen = []
    for i in range(45):
        zahlen.append(i+1)

    for i in range(6):
        zufallszahl = int(random.random() * (45-i)) + 1
        zahlen[44-i] = zahlen[zufallszahl-1]
        zahlen[zufallszahl-1] = 45-i

    return zahlen[39:]

def lottoziehung_statistik():
    dict = {}

    for i in range(45):
        dict[i+1] = 0

    for i in range(1000):
        zahlen = lottoziehung()
        for j in zahlen:
            dict[j] = dict[j] + 1

    for i in dict:
        print(str(i) + ": " + str(dict[i]))

print(lottoziehung())
lottoziehung_statistik()