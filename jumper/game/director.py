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
        self.play_another_time = 'y'
        self.letter = ""
        self.word = ""
        self.underscore = []
        self.jumper = []

    def start_game(self):
        """
        begins the game and continues running until the user decides to quit playing
        returns: --- (only calls other functions)
        """
        while self.play_another_time == 'y' and self.keep_playing:
            self.word = self.word_bank.get_word()
            self.underscore = self.screen.get_underscore(len(self.word))
            self.screen.display(len(self.word))

            while self.keep_playing and self.manager.game_over(self.word, self.underscore):
                self.get_inputs()
                self.update_values()
                self.output()

            self.play_again()

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

    def play_again(self):
        choice = input("Would you like to play again? [y/n]:")
        if choice == 'y':
            self.letter = ""
            self.word = ""
            self.underscore = []
            self.jumper = []
            self.screen.__init__()
            self.manager.__init__()
            self.word_bank.__init__()
        elif choice == 'n':
            self.keep_playing = False
