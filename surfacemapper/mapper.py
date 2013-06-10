"""Surface Mapper delegates rovers for mapping given rectangular grid area.

Mapper class is responsible for parsing user input and delegating mapping
task to the rovers.
"""

import sys

from rover import Rover
from mars_rover_controller import MarsRoverController
from mars_rover_instructions import MarsRoverInstructions


class Mapper(object):
    """Base class for delegating a mapping task to a rover."""

    def __init__(self):
        self.controller = None
        self.rovers = []

    def parse_input(self, user_input):
        """Parse user input into rover and gird endpoints."""
        user_input = user_input.split('\n')
        # grid co-ordinates
        grid_start = tuple(0, 0)
        grid_end = self.parse_grid_end(user_input[0])

        # initialize mars rover controller
        self.controller = MarsRoverController(grid_start, grid_end)

        # parse rovers position and initialize them
        rovers_with_instructions = zip(user_input[1::2], user_input[2::2])
        for id, rover in enumerate(rovers_with_instructions):
            self.parse_rover(id, rover)

    def parse_grid_end(self, grid_end):
        """Parse the grid endpoint string into a tuple."""
        try:
            return tuple([int(e) for e in grid_end.strip().split(' ')])
        except ValueError, e:
            raise ValueError('invalid grid endpoint, required int int')

    def parse_rover(self, id_, input):
        """Parse input and add rover along with instructions.

        Input rover: ('1 2 N', 'LMLMLMLMM')
        """
        point = input[0].strip().split(' ')
        if len(point) == 3:
            try:
                position = tuple([int(point[0]), int(point[1]), point[2].upper()])
            except ValueError:
                raise ValueError('Invalid rover position must be: int int str')

            instructions = [move.upper() for move in input[1].strip()]
            rover = Rover(id_, position, instructions)
            self.controller.add_rover(id_, rover)
            self.rovers.append(rover)
        else:
            raise Exception('Rover is not correctly specified.')

    def delegate(self):
        """Delegate each rover on its mapping task."""
        for rover in self.rovers:
            for instruction in rover.instructions:
                if instruction == 'L':
                    self.turn_left(rover)
                elif instruction == 'R':
                    self.turn_right(rover)
                elif instruction == 'M':
                    self.move(rover)
                else:
                    raise Exception('Unknown instruction %s for rover %r' %
                                    (instruction, rover))

    def turn_left(self, rover):
        """Turn the given rover left."""
        current_dir = rover.position[2]
        after_dir = MarsRoverInstructions.left_spin(current_dir)
        self.controller.turn(rover.id, after_dir)

    def turn_right(self, rover):
        """Turn the given rover right."""
        current_dir = rover.position[2]
        after_dir = MarsRoverInstructions.right_spin(current_dir)
        self.controller.turn(rover.id, after_dir)

    def move(self, rover):
        """Move the given rover one grid point."""
        current_dir = rover.position[2]
        next_point = MarsRoverInstructions.move_direction(current_dir)
        self.controller.move(rover.id, next_point)

    def show_stats(self):
        """Display the current grid point location for each rover."""
        for rover in self.rovers:
            print rover


def main():
    """Read user input and delegate mapping rovers."""

    if sys.stdin.isatty():
        user_input = ''
        grid_endpoint = raw_input(
            'Please enter upper-right coordinates of the plateau e.g. x y: ')
        user_input += grid_endpoint + '\n'
        while(True):
            rover = raw_input('Please enter rover position e.g. x y D: ')
            if rover == ('q' or 'quit'):
                break
            else:
                user_input += rover + '\n'
            instructions = raw_input('Please enter rover instructions: ')
            user_input += instructions + '\n'
    else:
        user_input = sys.stdin.read()

    if user_input[-1] == '\n':
        user_input = user_input[:-1]

    # delegate mapping rovers
    mapper = Mapper()
    mapper.parse_input(user_input)
    mapper.delegate()
    mapper.show_stats()


if __name__ == "__main__":
    main()
