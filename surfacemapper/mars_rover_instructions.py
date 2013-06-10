"""Provides interpretation of directions for moving a Mars rover.

Interpretation for any additional direction or a move, if required,
will be declared in this class.
"""


class MarsRoverInstructions(object):
    """Interpretation of directions for a Mars rover movement."""

    mdirection = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    lspin = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
    rspin = {'E': 'S', 'W': 'N', 'N': 'E', 'S': 'W'}

    @classmethod
    def move_direction(cls, direction):
        """Return move of a rover on grid according to its current direction."""
        try:
            return cls.mdirection[direction]
        except KeyError, e:
            raise KeyError('Invalid direction for moving forward: %s' %
                           direction)

    @classmethod
    def left_spin(cls, direction):
        """Resulting direction of rover after a left spin."""
        try:
            return cls.lspin[direction]
        except KeyError, e:
            raise KeyError('Invalid direction for a left spin: %s' %
                           direction)

    @classmethod
    def right_spin(cls, direction):
        """Resulting direction of rover after a right spin."""
        try:
            return cls.rspin[direction]
        except KeyError, e:
            raise KeyError('Invalid direction for a right spin: %s' %
                           direction)
