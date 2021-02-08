from rule_manager import RuleManager
from screen import Screen
from word_bank import WordBank


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
        self.manager = RuleManager()
        self.keep_playing = True
        pass

    def start_game(self):
        """
        begins the game and continues running until the user decides to quit playing
        returns: --- (only calls other functions)
        """

        while self.keep_playing and !manager.game_over:#TODO: make sure this is a method in rulemngr class:
            self.get_inputs()
            self.update_values()
            self.output()

    def get_inputs(self):
        self.word.pick_random_word()

        pass



    def update_values(self):
        """
        updates all values before outputting to screen
        returns: --- (only calls other functions)
        """


        pass

    def output(self):
        """
        prints to screen
        returns: ---(only calls other functions)
        """

        pass