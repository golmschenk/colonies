""" Contains Zone object and methods """
from .element import Element


class Zone(Element):

    """
    Zones are non-playable entities that exist on a board and have special properties.
    For example, a zone could destroy all objects that enter it, block entry by pieces,
    make all pieces immune to capture inside, etc.
    """

    def __init__(self, x, y, zone_type):
        """
        Constructor for Zone class.
        :param player: The player which controls this piece. 0 is no player.
        :type player: int
        :param x: The X coordinate of the piece.
        :type x: int
        :param y: The Y coordinate of the piece.
        :type y: int
        :param zone_type: What type of zone it is.
        :type zone_type: int
        """
        Element.__init__(self, x, y)
        self.type = zone_type
        self.collision = True  # All zones will have collision for now.
