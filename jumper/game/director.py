from game.rule_manager import Rule_Manager
from game.screen import Screen
from game.word_bank import WordBank


class Director:
    """
    The class director...
    """

    def __init__(self):
        """
        Creates objects of the classes
        """
        self.word = WordBank()
        self.screen = Screen()
        self.manager = Rule_Manager()
        self.keep_playing = True
        self.word_to_guess = ''

    def start_game(self):
        """
        begins the game and continues running until the user decides to quit playing
        returns: --- (only calls other functions)
        """
        self.word_to_guess = self.word.get_word()
        while self.manager.keep_playing:
            self.input_and_update_values()
            self.output()

   # def get_inputs(self):
   #     choice = self.screen.get_letter()
    #    return choice

    def input_and_update_values(self):
        """
        updates all values before outputting to screen
        returns: --- (only calls other functions)
        """
        self.manager.check_letter(self.screen.get_letter(), self.word_to_guess)
        self.screen.underscore(self.word_to_guess)

    def output(self):
        """
        prints to screen
        returns: ---(only calls other functions)
        """
        self.screen.display(self.word_to_guess)
