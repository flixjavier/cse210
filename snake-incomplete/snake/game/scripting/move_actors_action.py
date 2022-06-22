from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

class MoveActorsAction(Action):
    #** This class moves all the actors in the cast.

    def __init__(self):
        super().__init__()

    def execute(self, cast, script):
        """
        "Loop through all the actors in the cast and call the move_next() method on each one."
        
        Now let's look at the move_next() method
        
        :param cast: The cast of Actors in the game
        :param script: The script of Actions in the game
        """
        """ Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game. """
        # Override the execute(cast, script) method as follows:
        # 1) get all the actors from the cast
        actors = cast.get_all_actors()
        # 2) loop through the actors
        for actor in actors:
            actor.move_next()
        # 3) call the move_next() method on each actor
       
     

