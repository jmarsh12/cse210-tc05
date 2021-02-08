

class Screen():
    """
    The class jumper...
    """

    def __init__(self):
        self.jumper = ["  ___", " /___\\", " \   /",   "  \ /", "   0", "  /|\\", "  / \\", "\n^^^^^^^"]
        self.letter = ''
        self.underscore = []

    def get_letter(self):
        """
        get letter[a-z]
        return letter
        """
        self.letter = input("Guess a letter [a-z]: ")
        return self.letter

    def get_jumper(self):
        """
        return the list of jumber
        """
        return self.jumper
        
    def get_underscore(self, length):
        """
        get the number of "_" depending the number of letters in the word.
        """
        for i in range(length):
            self.underscore.append("_")
    
    def display(self, length):
        """
        display the list of "_" and jumper
        """
        for i in range(length):
            print(self.underscore[i], end = " ")
        
        print("\n")
    
        for i in self.jumper:
            print(i)
        
        print()
         
