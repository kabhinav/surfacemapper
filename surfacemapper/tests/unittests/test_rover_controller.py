import unittest


ROVER_ID = 1
ROVER_ID2 = 2

class TestRoverController(unittest.TestCase):

    def setUp(self):
        from surfacemapper.rover import Rover
        from surfacemapper.rover_controller import RoverController

        self.controller = RoverController((0, 0), (5, 5))
        self.rover = Rover(ROVER_ID, (1, 2, 'N'), ['L', 'M'])

    def tearDown(self):
        self.controller = None
        self.rover = None

    def test_add_rover(self):
        self.assertEqual(self.controller.rovers, {})
        self.controller.add_rover(ROVER_ID, self.rover)
        self.assertEqual(self.controller.rovers, {ROVER_ID: self.rover})

    def test_add_rover_exception(self):
        from surfacemapper.rover import Rover
        self.controller.add_rover(ROVER_ID, self.rover)
        new_rover = Rover(ROVER_ID2, (1, 2, 'N'), ['L', 'M'])
        with self.assertRaises(Exception):
            self.controller.add_rover(ROVER_ID, new_rover)

    def test_check_grid_position(self):
        self.controller.check_grid_position((1, 2, 'N'))

    def test_check_grid_position_not_empty(self):
        self.controller.add_rover(ROVER_ID, self.rover)
        with self.assertRaises(Exception):
            self.controller.check_grid_position((1, 2, 'N'))

    def test_check_grid_position_not_in_grid(self):
        with self.assertRaises(Exception):
            self.controller.check_grid_position((1, 6, 'N'))
