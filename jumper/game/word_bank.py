import random


class WordBank:
    """
    The class WordBank deals with creating a word and randomly picking that word
    to return to the class Screen.
    """

    def __init__(self):
        """
        The constructor method.
        """
        self.pick_random_word = ''
        self.generate_word = []
        pass

    def generate_word(self):
        """
        The generate_word method contains a list of words to choose from.
        """
        words = ['Intelligent', 'Supercalifragilisticexpialidocious', 'Gina', 'Pterodactyl', 'Giraffe', 'Dragon',
                 'Hippopotomonstrosesquippedaliophobia']

        return words
        pass

    def pick_random_word(self):
        """
        The pick_random_word method takes the list from generate_word and picks
        a random one to return to Screen.
        """
        pass

    pass
