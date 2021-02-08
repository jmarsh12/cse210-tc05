from screen import Screen
import sys

class Rule_Manager():
    """
    The class Rule_Manager takes care of 
    methods relating to the gameplay of the user.
    """

    def __init__(self):
        self.play = 0

    def check_letter(self, screen.letter, rand_word):
        for i in rand_word
            if screen.letter is == i:
                return True
            else:
                return False
        """
        This function will take the letter that it recieves from screen and check
        to see if it is a letter in the word that the player is guessing. 
        It will return a true or false.
        """

    def wrong_answer(self):
    """
    This function keeps track of how many times 
    the player has guessed the wrong answer.
    """
        if check_letter == False:
             self.play += 1
        
    def keep_playing(self)
    """
    This function will run continously and determine 
    whether or not you can keep playing.
    """
    while self.play >= 3
    exit()