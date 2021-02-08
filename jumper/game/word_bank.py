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
