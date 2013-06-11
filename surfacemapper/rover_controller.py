
class RoverController(object):
    """Base controller class for a rover."""

    def __init__(self, grid_origin, grid_end):
        """Create a rover controller.

        Input params:
        'grid_origin': lower left hand side co-ordinates of the grid,
                        default (0, 0).
        'grid_end': upper right hand side co-ordinates of the grid.
        """
        self.rovers = {}
        self.grid_origin = grid_origin
        self.grid_end = grid_end
        self.directions = ['E', 'W', 'N', 'S']

    def add_rover(self, rover_id, rover):
        """Check rover's position and add rover to the list of rovers
        controlled by the RoverController.
        """
        self.check_grid_position(rover.position)
        if not rover_id in self.rovers.keys():
            self.rovers[rover_id] = rover

    def move(self, rover_id, grid_point):
        """Moves the rover with id to the input grid point.

        Must be overridden by subclass.
        """

    def turn(self, rover_id, new_direction):
        """Turn the rover with id in the new direction.
        overridden in subclass."""

    def check_grid_position(self, position):
        """Checks the input grid position.

        The input grid position should be within the grid boundries
        and it should be empty, i.e., no other rover should be present.
        """
        if not self.is_empty(position):
            raise Exception('Another rover is already present at location')

        if not self.inside_grid(position):
            raise Exception('New rover position is not with in the grid.')

    def is_empty(self, position):
        """Checks if a grid position is empty or not."""
        for rover in self.rovers.values():
            if position == rover.position:
                return False

        return True

    def inside_grid(self, position):
        """Checks if a position lies with in the grid."""
        x, y, d = position
        if (x < self.grid_origin[0]) or (x > self.grid_end[0]):
            return False
        elif (y < self.grid_origin[1]) or (y > self.grid_end[1]):
            return False

        return True

    def check_rover_direction(self, direction):
        """Checks if an input direction is valid."""
        if direction not in self.directions:
            raise Exception('Invalid turn direction for rover.')
