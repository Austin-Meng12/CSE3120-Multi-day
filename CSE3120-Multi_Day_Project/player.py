# player class in player.py
import dice
from dice import Die
from random import randint

class Player:


    def __init__(self,NAME, DICE_AMOUNT = 5,):
        """
        Creates the player object
        """
        self.NAMES = NAME
        self.DICE = []   # The 5 dices
        self.FOUND = []  # The list when they find 4,5,6
        self.TURN = 0
        self.MAX_TURN = 3
        self.SCORE = 0

        # the pirate Crew is not found
        self.SHIP = False
        self.CAPTAIN = False
        self.CREW = False
        self.CHANCE = True
        self.SPECIALDICE = 0
        for i in range(DICE_AMOUNT):
            self.DICE.append(Die())
    def rollDice(self):
        """
        Rolls the dice
        """
        for die in self.DICE:
            die.rollDie()



    def displayDice(self): # THis is needed for testing (dont really need it for the program tho)  (output)
        for i in range(len(self.DICE)):
            print(f"Die {i + 1}: {self.DICE[i].DIE_NUMBER}")
    def displayFound(self): # this is also for testing (output)
        for i in range(len(self.FOUND)):
            print(f"Die Found: {self.FOUND[i].DIE_NUMBER}")


    def determineEntire(self):   #processing

        """
        Function that determines the ship, capatian, and crew, and the amount of gold that is within
        """

        while self.getTurn() < self.MAX_TURN:  # Checking whether or not we are under 3 turns
            self.rollDice()  # rerolls the dice you have
            print(f"{self.NAMES}'s {self.getTurn() + 1} turn")
            if self.SHIP == False:  # checking if there is a ship (number 6)
                for i in range(self.getDiceLength()):
                    if self.DICE[i].DIE_NUMBER == 6:
                        print("ship is found")
                        self.FOUND.append(self.DICE.pop(i))
                        self.SHIP = True
                        break

            if self.SHIP == True and self.CAPTAIN == False:  # checking for captain
                for i in range(self.getDiceLength()):
                    if self.DICE[i].DIE_NUMBER == 5:
                        print("captain is found")
                        self.FOUND.append(self.DICE.pop(i))
                        self.CAPTAIN = True
                        break

            if self.SHIP == True and self.CAPTAIN == True and self.CREW == False:  # checking for crew
                for i in range(self.getDiceLength()):
                    if self.DICE[i].DIE_NUMBER == 4:
                        print("Crew is found")
                        self.FOUND.append(self.DICE.pop(i))
                        self.CREW = True
                        break
            if self.SHIP == True and self.CAPTAIN == True and self.CREW == True:  # caculating the amount of gold the player as

               self.caculategold()

            self.addTurn()
            if self.getTurn() == 3 and self.CREW == False:  # After 3 turns, and they still haven't found the crew yet
                print("you suck you found zero gold, skill issue get better")
            input()  # pressing enter again to "contiune/move on"

    def caculategold(self):   #process
        """
        This caculates the amount of gold and asking if they want to reroll
        """

        for i in range(self.getDiceLength() - 1):
            GOLD = self.DICE[i].DIE_NUMBER + self.DICE[i + 1].DIE_NUMBER
            print(f"you found {GOLD} coins")
            self.oldscore(GOLD)


            if self.getTurn() < self.MAX_TURN - 1:  # asking if they want to reroll their two leftover dices
                ANSWER = input("Keep the Dice? (y/n):")
                if ANSWER.upper() == "N":
                    self.newScore(GOLD)
                    break
                else:  # if they keep their coins (finish their turn completely)
                    self.addTurn()
                    self.addTurn()



    def fiftyfiftydice(self):  # this is a small extension i added , they can reroll 1 more dice out side of their 2 dice they already have for more points
        """
        They can reroll a 15 sideded dice for a chance to gain or lose more points
        """
        if self.SHIP == True and self.CAPTAIN == True and self.CREW == True:  # This extra dice can only be used if they have found ship, capatian, and crew
            SPECIAL = input("Do you want to risk your coins for more coins (y/n):")
            self.SPECIALDICE = randint(1 , 15) # generatates a random number between 1 and 15

            if SPECIAL.upper() == "Y":
                self.CHANCE = True
                if self.SPECIALDICE > 10:   # if its bigger than 10, they can get 10 more coins
                    self.specialdicebigger()
                elif self.SPECIALDICE < 10: # if its smaller than 10, they lose 10 points
                    self.specialdicesmaller()
                    if self.SCORE < 0:  # there can't be a negative score/points
                        self.specialdicezero()
                elif self.SPECIALDICE == 10:  # if they roll a ten they gain 20 points
                    self.specialdiceten()
            else:
               self.CHANCE = False
               self.origionalscore()

    def specialdicezero(self):
        """
        Makes the Player score zero
        self.SCORE = int
        """

        self.SCORE = 0
    def specialdicebigger(self):
        """
        Add ten to their current score
        self.SCORE = int
        """
        self.SCORE = self.SCORE + 10
    def specialdicesmaller(self):
        """
        subtract 10 from their current score
        self.SCORE = int
        """
        self.SCORE = self.SCORE - 10
    def origionalscore(self):
        """
        Leaves their score without any change
        self.SCORE = int
        """
        self.SCORE = self.SCORE

    def specialdiceten(self):
        self.SCORE = self.SCORE + 20


    def oldscore(self, score):  # this is the score before we ask if they want to keep
        """
        The score the player gold stays the same
        score: int
        """
        self.SCORE = score
    def newScore(self, score):  # this is the score after they say no to keeping
        """
        If they say yes, to rerolling, they reroll their dice and
        score:int
        """
        self.SCORE = score

    def resetPlayer(self, DICE_AMOUNT = 5):
        """
        resets the player variables and attributes

        """
        self.FOUND = []
        self.DICE = []
        for i in range(DICE_AMOUNT):
            self.DICE.append(Die())
        self.TURN = 0
        self.SCORE = 0

        self.SHIP = False
        self.CAPTAIN = False
        self.CREW = False





    def getScore(self):  #accessor methods
        """
        gets each of the player's score
        return: int (Player score)

        """
        return self.SCORE

    def addTurn(self):
        """
        add 1 to each turn
        """
        self.TURN +=1
    def getTurn(self): # accessor Methods
        """
        gets what turn each player is on
        return: int
        """
        return self.TURN

    def __str__(self):
        return self.NAMES

    def getDiceLength(self): # accessor Methods
        """
        Gets the number of dices you still have
        return: length of a list

        """
        return len(self.DICE)






