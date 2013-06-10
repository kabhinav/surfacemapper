from rover_controller import RoverController


class MarsRoverController(RoverController):
    """Controller for a Mars based rover."""

    def move(self, rover_id, grid_point):
        """Move rover id to its new location."""
        rover = self.rovers[rover_id]
        x, y, d = rover.position

        # Compute new rover position, direction will remain same
        x += grid_point[0]
        y += grid_point[1]
        new_position = (x, y, d)

        # Check new grid postion
        self.check_grid_position(new_position)

        # Set the rover's new position
        rover.position = new_position

    def turn(self, rover_id, direction):
        """Turn rover with id to its new direction."""
        rover = self.rovers[rover_id]
        x, y, d = rover.position

        # Compute new rover position, heading will change to new direction
        # (x, y) will remain unchanged
        new_position = (x, y, direction)

        # Check new grid postion
        self.check_grid_position(new_position)

        # Set the rover's new position
        rover.position = new_position
