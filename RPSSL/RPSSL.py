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
    pick = ""
    while pick not in figure.figureList():
        pick = input("Choose from Scissors, Paper, Rock, Lizard, Spock:")
    return figure(pick, figure.figureBeats(pick))

def comPick(mode):
    match mode:
        case 0:
            rand = random.randrange(0,5,1)
            fig = figure.figureList()[rand]
            return figure(fig, figure.figureBeats(fig))
        case 1:
            with open('RPSSL/RPSSL.json', 'r') as file:
                data = json.load(file)
                #TODO: Schweren spielmodus bauen

def compare(fig1, fig2):
    return (fig2.fig in fig1.beats,  fig1.fig == fig2.fig)

def stats(upick, cpick):
    with open('RPSSL/RPSSL.json', 'r+') as file:
        data = json.load(file)
        data["user"][upick.fig] += 1
        data["com"][cpick.fig] += 1
        if compare(upick, cpick)[0] and not compare(upick, cpick)[1]:
            data["user"]["wins"] += 1
        elif not compare(upick, cpick)[1]:
            data["com"]["wins"] += 1
        else: 
            data["draws"] += 1
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def play(pick, mode):
    upick = pick if type(pick) == figure else figure(pick, figure.figureBeats(pick))
    cpick = comPick(mode)
    stats(upick, cpick)
    if compare(upick, cpick)[0] and not compare(upick, cpick)[1]:
        return 'User Wins! User pick: ' + upick.fig + ', Com Pick: ' + cpick.fig
    elif not compare(upick, cpick)[1]:
        return 'Com Wins! User pick: ' + upick.fig + ', Com Pick: ' + cpick.fig
    else:
        return 'Draw! User pick: ' + upick.fig + ', Com Pick: ' + cpick.fig

def main():
    print(play(userPick()), 0)

if __name__ == "__main__":
    comPick(1)