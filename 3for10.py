import random

class Game():

    deck = [
            "AH","AD","AS","AC",
            "2H","2D","2S","2C",
            "3H","3D","3S","3C",
            "4H","4D","4S","4C",
            "5H","5D","5S","5C",
            "6H","6D","6S","6C",
            "7H","7D","7S","7C",
            "8H","8D","8S","8C",
            "9H","9D","9S","9C",
            "10H","10D","10S","10C",
            "KH","KD","KS","KC",
            "QH","QD","QS","QC",
            "JH","JD","JS","JC",
            "JO","JO"
            ]

    

    moneyPot = 10

    def __init__(self) -> None:
        pass

    def setOf(n,simStat=False):
        num = 0
        while num < n:
            Game.main(inSim = simStat)
            num += 1

    @classmethod
    def main(self,inSim=False):

        inputNum = 3
        count =0
        choiceCard = []
        
        if inSim:
            choiceCard = random.sample(Game.deck,3)
        else:
            print("Seven of hearts => 7H")
            print("Black, Red, Red => B,R,R")

            while count < inputNum:
                card = input("enter card : ")
                choiceCard.append(card)
                count += 1
        

        if not (choiceCard[0] != choiceCard[1] != choiceCard[2]) and not (choiceCard[0] == "JO" or choiceCard[1] == "JO" or choiceCard[2] == "JO"):
            raise ValueError ("All chosen cards must be unique")

        dealCard = random.sample(Game.deck,3)

        score = 0

        for i in choiceCard:
            if i in dealCard:
                score += 1
            else:
                pass
        
        if (dealCard[0] == "JO" or dealCard[1] == "JO" or dealCard[2] == "JO") and Game.moneyPot > 0:
            Game.moneyPot *= 2

        print(dealCard)

        if score == 3:
            Game.moneyPot += 10
        elif score == 2:
            Game.moneyPot += 5
        elif score == 1:
            Game.moneyPot += 2
        else:
            Game.moneyPot = Game.moneyPot - 10

        print(Game.moneyPot)

class Simulate():

    inSim = False

    def __init__(self) -> None:
        inSim = True

    def sim(self,n):
        simCount = 0
        while simCount < n:
            Game.main(inSim=True)
            simCount += 1
        print(Game.moneyPot)


# Game.setOf(10)
S = Simulate()
S.sim(10000)