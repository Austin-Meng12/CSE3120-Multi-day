# game.py


from player import Player
from dice import Die
class Game:


    def __init__(self):
        """
        The attributes for the game class
        """
        self.displayTitle()     # The title screen for the program
        self.createPlayers()    # creating the player object within the game
        self.rungame = True
        self.ROUND = 0         # The number of rounds it starts at

        self.PLAYERSCORE = []    # A list that contains all the player scores
    def run(self):
        while self.rungame == True:
            self.addround()

            print(f"ROUND {self.ROUND}")
            input()

            for PLAYER in self.PLAYERS:

                PLAYER.determineEntire()
                PLAYER.fiftyfiftydice()


            #OUTPUT (scoreboard, and PLAYER score and who wins)
                if PLAYER.SHIP == True and PLAYER.CAPTAIN == True and PLAYER.CREW == True and PLAYER.CHANCE == True:
                    if PLAYER.SPECIALDICE < 10:
                        print(f"Unlucky, you lost, your score is {PLAYER.getScore()}")
                    elif PLAYER.SPECIALDICE >= 10:
                        print(f"Congrats, you won, your new score is {PLAYER.getScore()}")
                if PLAYER.SHIP == True and PLAYER.CAPTAIN == True and PLAYER.CREW == True and  PLAYER.CHANCE == False:
                    print(f"Your score is still {PLAYER.getScore()}")


            print("The scoreboard: ")
            for PLAYER in self.PLAYERS:    # Shows the score for each person

                print(f"{PLAYER}: {PLAYER.getScore()} coins")
                self.PLAYERSCORE.append(PLAYER.getScore())


                # determining who wins
            self.PLAYERSCORE.sort()  # sorts the Player

            if self.PLAYERSCORE[self.getplayerlength()- 1] == self.PLAYERSCORE[self.getplayerlength() - 2]:
                print("No one wins")     # this is to see wheter or not the last index is equal to the second last index (meaning a tie and no winner)
            else:
                # to see if the last index is larger than the second last index
                for i in range(len(self.PLAYERS)):
                    if self.PLAYERSCORE[self.getplayerlength() - 1] == self.PLAYERS[i].getScore():
                        print(f"{self.PLAYERS[i]} Wins")
                        break



            for PLAYER in self.PLAYERS:    # after each round resets the player and the scores
                PLAYER.resetPlayer()
                self.PLAYERSCORE = []
            if self.ROUND == 10:
                self.rungame = False
                exit()

    def createPlayers(self): #input
        """
        Creates the player for the game
        return: list (with the player names inside)
        """
        PLAYERS = int(input("How many Players:"))
        self.PLAYERS = []

        for i in range(PLAYERS):
            self.PLAYERS.append(Player(input(f"Player {i+1} Name:")))

    def getplayerlength(self):  #accessor
        """
        How many players are playing
        return: int (the length of the list)
        """
        return len(self.PLAYERS)
    def displayTitle(self):
        """
        Starting screen

        """

        print("Welcome to ship Captain Crew")
        print("Press enter to start and to play the game")

    def addround(self):
        """
        add 1 round
        """
        self.ROUND += 1
    def getround(self): #accessor
        """
        Gets the round the players are on
        returnL int (The round number)
        """
        return self.ROUND




if __name__ == "__main__":
    GAME = Game()
    GAME.run()
