"""
title: dice class for the game
Author: Austin Meng
date -  created: 2023 - 03 - 22

"""
from random import randint

class Die:
    """
    Create die objects to roll for random numbers

    """

    def __init__(self, HIGHEST_NUMBER = 6):
        # constructor for the object
        self.DIE_MAX_NUMBER = HIGHEST_NUMBER
        self.DIE_NUMBER = 0
        self.VALUE = self.DIE_NUMBER



    def rollDie(self):
        """
        randomly roll a number for a self.DIE_NUMBER
        :return: none

        """

        self.DIE_NUMBER = randint(1, self.DIE_MAX_NUMBER)
    def getValue(self):

        return self.DIE_NUMBER




if __name__ == "__main__":

    Die_1 = Die()
    Die_1.rollDie()
    Die_1.getValue()
    print(Die_1.DIE_NUMBER)





