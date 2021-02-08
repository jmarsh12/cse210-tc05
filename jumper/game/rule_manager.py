class Rule_Manager():
    """
    The class Rule_Manager takes care of 
    methods relating to the gameplay of the user.
    """

    def __init__(self):
        self.play = 0
        self.index = []
        self.correct_letter = ""

    def check_letter(self, letter, rand_word):
        for i in rand_word:
            if letter == i.lower():
                return True
        return False
        """
        This function will take the letter that it recieves from screen and check
        to see if it is a letter in the word that the player is guessing. 
        It will return a true or false.
        """
    
    def get_correct_letter(self, letter, word):
        """
        get the correct letter and the index for chainging the list of underscore
        """
        self.index.clear()
        for i in range(len(word)):
            if letter == word[i:i+1].lower():
                self.index.append(i)
                self.correct_letter = letter
    
    def change_underscore(self, underscore):
        """
        change the list of underscore to correct letter
        """
        for i in self.index:
            if i == 0:
                underscore[i] = self.correct_letter.upper()
            else:
                underscore[i] = self.correct_letter

    def wrong_answer(self, jumper):
        """
        This function keeps track of how many times 
        the player has guessed the wrong answer.
        """
        # while check_letter == True:
        jumper.pop(0)
        self.play += 1
        if self.play == 4:
            jumper[0] = "   x"
        
    def game_over(self, word, underscore):
        """
        This function will run continously and determine 
        whether or not you can keep playing.
        """
        if self.play >= 4:
            print(f"Game over. The word is {word}")
            return False
        for i in underscore:
            if i == "_":
                return True
        print("You won.")
        return False