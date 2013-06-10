"""Rover model."""


class Rover(object):
    """Rover class"""

    def __init__(self, id_, position, instructions):
        self.id = id_
        self.position = position
        self.instructions = instructions

    def __repr__(self):
        """Rover string representation."""
        return '%s %s %s\n' % (self.position[0], self.position[1],
                               self.position[2])

    def _set_instructions(self, instructions):
        """Set the Rover's instructions."""
        if isinstance(instructions, list):
            self._instructions = instructions
        else:
            raise ValueError('instructions must be a list.')

    def _get_instructions(self):
        """Return the Rover's instructions."""
        return self._instructions

    def _set_position(self, position):
        """Set the Rover's position."""
        if isinstance(position, tuple) and len(position) == 3:
            self._position = position
        else:
            raise ValueError('position must be tuple of length 3.')

    def _get_position(self):
        """Return the Rover's position."""
        return self._position

    # rover properties
    position = property(_get_position, _set_position, None)
    instructions = property(_get_instructions, _set_instructions, None)
