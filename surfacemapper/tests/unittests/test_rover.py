import unittest


ROVER_ID = 1
POSITION = (1, 2, 'N')
INVALID_POS = (1, 2)
INSTRUCTIONS = ['L', 'M']
INVALID_INS = []

class TestRover(unittest.TestCase):

    def test_create_rover(self):
        from surfacemapper.rover import Rover

        rover = Rover(ROVER_ID, POSITION, INSTRUCTIONS)
        self.assertEqual(rover.id, ROVER_ID)
        self.assertEqual(rover.position, POSITION)
        self.assertEqual(rover.instructions, INSTRUCTIONS)

    def test_rover_repr(self):
        from surfacemapper.rover import Rover

        rover = Rover(ROVER_ID, POSITION, INSTRUCTIONS)
        expected = '1 2 N\n'
        self.assertEqual('%r' % rover, expected)

    def test_create_rover_position_exception(self):
        from surfacemapper.rover import Rover

        with self.assertRaises(ValueError):
            Rover(ROVER_ID, INVALID_POS, INSTRUCTIONS)

    def test_create_rover_instructions_exception(self):
        from surfacemapper.rover import Rover

        with self.assertRaises(ValueError):
            Rover(ROVER_ID, POSITION, INVALID_INS)



