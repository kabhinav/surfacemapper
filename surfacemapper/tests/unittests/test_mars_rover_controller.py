import unittest


ROVER_ID = 1


class TestMarsRoverController(unittest.TestCase):

    def setUp(self):
        from surfacemapper.rover import Rover
        from surfacemapper.mars_rover_controller import MarsRoverController

        self.controller = MarsRoverController((0, 0), (5, 5))
        rover = Rover(ROVER_ID, (1, 2, 'N'), ['L', 'M'])
        self.controller.add_rover(ROVER_ID, rover)

    def tearDown(self):
        self.controller = None

    def test_move(self):
        self.controller.move(ROVER_ID, (0, 1))
        rover = self.controller.rovers[ROVER_ID]
        self.assertEqual((1, 3, 'N'), rover.position)

    def test_move_invalid_grid_point(self):
        with self.assertRaises(Exception):
            self.controller.move(ROVER_ID, (-2, 0))

    def test_turn(self):
        self.controller.turn(ROVER_ID, 'E')
        rover = self.controller.rovers[ROVER_ID]
        self.assertEqual((1, 2, 'E'), rover.position)

    def test_turn_invalid_direction(self):
        with self.assertRaises(Exception):
            self.controller.turn(ROVER_ID, 'NE')
