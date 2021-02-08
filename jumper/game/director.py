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
        self.word_bank = WordBank()
        self.screen = Screen()
        self.manager = Rule_Manager()
        self.keep_playing = True
        self.letter = ""
        self.word = ""
        self.underscord = []
        self.jumber = []
        
    def start_game(self):
        """
        begins the game and continues running until the user decides to quit playing
        returns: --- (only calls other functions)
        """
        self.word = self.word_bank.get_word()
        self.underscore = self.screen.get_underscore(len(self.word))
        self.screen.display(len(self.word))
        while self.keep_playing and self.manager.game_over(self.word, self.underscore):#TODO: make sure this is a method in rulemngr class:
            self.get_inputs()
            self.update_values()
            self.output()

    def get_inputs(self):
        self.letter = self.screen.get_letter()
        self.jumper = self.screen.get_jumper()

    def update_values(self):
        """
        updates all values before outputting to screen
        returns: --- (only calls other functions)
        """
        if self.manager.check_letter(self.letter, self.word):
            self.manager.get_correct_letter(self.letter, self.word)
            self.manager.change_underscore(self.underscore)
        else:
            self.manager.wrong_answer(self.jumper)

    def output(self):
        """
        prints to screen
        returns: ---(only calls other functions)
        """
        self.screen.display(len(self.word))
        