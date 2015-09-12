""" Contains Element object and methods """


class Element:

    """
    An element has the minimium amount of detail that can
    allow something to exist on and be displayed for a game board.
    """

    def __init__(self, x, y):
        """
        Constructor for Element.
        :param x: The X coordinate of the piece.
        :type x: int
        :param y: The Y coordinate of the piece.
        :type y: int
        """
        self.x = x
        self.y = y
