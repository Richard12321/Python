import random

def lottoziehung(zahlenvon, zahlenbis, gezogene):
    zahlen = []
    for i in range(zahlenbis-zahlenvon):
        zahlen.append(zahlenvon+i+1)

    for i in range(gezogene):
        zufallszahl = random.randrange(zahlenvon, zahlenbis)
        zahlen[len(zahlen)-i-1], zahlen[zufallszahl-zahlenbis] = zahlen[zufallszahl-zahlenbis], zahlen[len(zahlen)-i-1]

    return zahlen[len(zahlen)-gezogene:]

def lottoziehung_statistik(zahlenvon, zahlenbis, gezogene, ziehungen):
    dict = {}

    for i in range(zahlenbis-zahlenvon):
        dict[zahlenvon+i+1] = 0

    for i in range(ziehungen):
        zahlen = lottoziehung(zahlenvon,zahlenbis, gezogene)
        for j in zahlen:
            dict[j] = dict[j] + 1

    for i in dict:
        print(str(i) + ": " + str(dict[i]))


print(lottoziehung(0,45,6))
lottoziehung_statistik(0,45,6,1000)