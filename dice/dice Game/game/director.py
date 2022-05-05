from game.die import Die

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Welcome to Dice Game.\nAre you Willing To Risk Everything?\nRoll the dice and get surprised.")
        print("Points:\n1's = 100\n5's = 50\nIf you do not roll at least one 1 or 5,\nGAME OVER!!!\n")
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        roll_dice = input("Roll dice? [y/n] ")
        if roll_dice == "y" or roll_dice== "yes":
            self.is_playing = True
        elif roll_dice == "n" or roll_dice== "no":
            print("\nOh you don't want to risk it all!\nThanks for playing")
            self.is_playing = False
        else:
            """ If the user press another key, display an error """
            print("Wrong Input! Try again.")
            roll_dice = input("Roll dice? [y/n] ")
        """ self.is_playing = (roll_dice == "y") """
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        #*I set the self.score to 0, because when the user roll the dice, 
        #*and even when the user gets no 1's and 5's, the game continue. With this change, if you
        #*roll the dices and you do not get 1's or 5's, the game stops. 
        self.score=0
        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points
        """ print(f"the dice score is {self.score}") """
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "
        print(f"You rolled: {values}")
        #*Game Over message, when the player gets no 1's or 5's. 
        if self.score == 0:
            print("Sorry, You did not get any 1's or 5's!!!\nGAME OVER")
            self.is_playing = False
        else:
            print(f"Your score is: {self.total_score}\n")
            self.is_playing == (self.score > 0)