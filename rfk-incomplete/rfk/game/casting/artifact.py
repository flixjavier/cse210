from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

# > The `Artifact` class is a subclass of the `Actor` class. It has one additional attribute,
# `_message`, and two additional methods, `get_message` and `set_message`
class Artifact(Actor):
    def __init__(self):
        """
        The function __init__() is a constructor that initializes the class
        """
        super().__init__()
        self._message=""
    
    def get_message(self):
        """
        It returns the value of the private variable _message
        :return: The message is being returned.
        """
        return self._message

    def set_message(self,message):
        """
        The function set_message() takes a parameter called message and assigns it to the attribute
        _message
        
        :param message: The message to be displayed
        """
        self._message=message




        