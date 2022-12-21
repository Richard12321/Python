import random
import json

class figure():
    def __init__(self, fig, beats):
        self.fig = fig
        self.beats = beats

    def figureList():
        return ["Scissors", "Paper", "Rock", "Lizard", "Spock"]

    def figureBeats(pick):
        match pick:
            case "Scissors":
                return ["Paper", "Lizard"]
            case "Paper":
                return ["Spock", "Rock"]
            case "Rock":
                return ["Lizard", "Scissors"]
            case "Lizard":
                return ["Spock", "Paper"]
            case "Spock":
                return ["Scissors", "Rock"]
             
def userPick():
    mode = ""
    pick = ""
    while mode not in ["easy","hard"]:
        mode = input("Choose gamemode from easy, hard:")
    while pick not in figure.figureList():
        pick = input("Choose from Scissors, Paper, Rock, Lizard, Spock:")
    return figure(pick, figure.figureBeats(pick)), 0 if mode == "easy" else 1

def comPick(mode, lastPick, player):
    match mode:
        case 0:
            rand = random.randrange(0,5,1)
            cfig = figure.figureList()[rand]
            return figure(cfig, figure.figureBeats(cfig))
        case 1:
            with open("RPSSL/RPSSL.json", "r") as file:
                data = json.load(file)
                data = data["players"][str(player)]["user"]
                mostCommon = (0, "")
                for i in figure.figureList():
                    if data[i] > mostCommon[0]:
                        mostCommon = (data[i], i)
                beats = []
                for i in figure.figureList():
                    if mostCommon[1] in figure.figureBeats(i):
                        beats.append(figure(i, figure.figureBeats(i)))
                ra = random.randrange(0,2,1)
                return beats[ra] if beats[ra] != lastPick else beats[1-ra]


def compare(fig1, fig2):
    return (fig2.fig in fig1.beats,  fig1.fig == fig2.fig)

def stats(upick, cpick, player):
    with open('RPSSL/RPSSL.json', 'r+') as f:
        data = json.load(f)
        if player in data["players"]:
            data["players"][str(player)]["user"][upick.fig] += 1
            data["players"][str(player)]["com"][cpick.fig] += 1
        else:
            y = {player: { "player" : { "won" : 0, "Scissors" : 0, "Paper" : 0, "Rock" : 0, "Lizard" : 0, "Spock" : 0},"com" : { "won" : 0, "Scissors" : 0, "Paper" : 0, "Rock" : 0, "Lizard" : 0, "Spock" : 0},"draw":0}}
            data["players"].update(y)
            data["players"][str(player)]["user"][upick.fig] += 1
            data["players"][str(player)]["com"][cpick.fig] += 1
            if compare(upick, cpick)[0] and not compare(upick, cpick)[1]:
                data["user"]["wins"] += 1
            elif not compare(upick, cpick)[1]:
                data["com"]["wins"] += 1
            else: 
                data["draws"] += 1
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


def play(pick, mode, lastPick, player):
    upick = pick if type(pick) == figure else figure(pick, figure.figureBeats(pick))
    cpick = comPick(mode, lastPick, player)
    stats(upick, cpick, player)
    if compare(upick, cpick)[0] and not compare(upick, cpick)[1]:
        return 'User Wins! User pick: ' + upick.fig + ', Com Pick: ' + cpick.fig
    elif not compare(upick, cpick)[1]:
        return 'Com Wins! User pick: ' + upick.fig + ', Com Pick: ' + cpick.fig
    else:
        return 'Draw! User pick: ' + upick.fig + ', Com Pick: ' + cpick.fig

def main():
    player = input("Player name:")
    u = userPick()
    print(play(u[0], u[1], "", player))

if __name__ == "__main__":
    main()