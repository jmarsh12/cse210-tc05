from game.rule_manager import RuleManager
from game.screen import Screen
from game.word_bank import WordBank


class Director():
    """
    The class director...
    """

    def __init__(self):
        """
        
        """
        #self.console = Console()
        #self.jumper = Jumper()
       # self.bard = Board()
        #self.board.debug_mode = False
        self.keep_playing = True
        #self.current_guess = ''
        pass

    word1 = WordBank()
    screen1 = Screen()
    manager = RuleManager()

    def start_game(self):
        """
        begins the game and continues running until the user decides to quit playing
        """
        while self.keep_playing and !manager.game_over: #TODO: make sure this is a method in rulemngr class
            pass
        pass

    def update_values(self):
        """
        updates all values before outputting to screen
        """
        pass

    def output(self):
        """
        prints to screen
        """
        pass