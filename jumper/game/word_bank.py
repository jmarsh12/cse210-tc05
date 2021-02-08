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
        self.get_word = []

    def get_word(self):
        """
        The generate_word method contains a list of words to choose from, as well as
        picks a random word to return to the user.
        """
        self.get_word = ['Intelligent', 'Supercalifragilisticexpialidocious', 'Gina', 'Pterodactyl', 'Giraffe',
                         'Dragon',
                         'Hippopotomonstrosesquippedaliophobia']
        word = random.choice(self.get_word)

        return word.upper()

    def pick_random_word(self):
        """
        The pick_random_word method takes the list from generate_word and picks
        a random one to return to Screen.
        """
        # TODO do we need this method?
        pass
