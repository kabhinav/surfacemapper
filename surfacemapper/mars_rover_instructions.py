
class MarsRoverInstructions(object):
    """Provides interpretation of directions for moving a Mars rover.

    Interpretation for any additional direction, if required, can be
    declared here.
    """

    move_direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    left_spin = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
    right_spin = {'E': 'S', 'W': 'N', 'N': 'E', 'S': 'W'}

    @classmethod
    def move_direction(cls, direction):
        """Return move of a rover on grid according to its direction."""
        try:
            return cls.move_direction[direction]
        except KeyError:
            raise Exception('Invalid direction for moving forward: %s' %
                            direction)

    @classmethod
    def left_spin(cls, direction):
        """Resulting direction of rover after a left spin."""
        try:
            return cls.left_spin[direction]
        except KeyError:
            raise Exception('Invalid direction for a left spin: %s' %
                            direction)

    @classmethod
    def right_spin(cls, direction):
        """Resulting direction of rover after a right spin."""
        try:
            return cls.right_spin[direction]
        except KeyError:
            raise Exception('Invalid direction for a right spin: %s' %
                            direction)
