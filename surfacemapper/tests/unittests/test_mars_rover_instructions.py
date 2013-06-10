import unittest

from surfacemapper.mars_rover_instructions import MarsRoverInstructions

class TestMarsRoverInstructions(unittest.TestCase):

    def test_move_directions(self):
        move = MarsRoverInstructions.move_direction('E')
        self.assertEqual(move, (1, 0))

        move = MarsRoverInstructions.move_direction('W')
        self.assertEqual(move, (-1, 0))

        move = MarsRoverInstructions.move_direction('N')
        self.assertEqual(move, (0, 1))

        move = MarsRoverInstructions.move_direction('S')
        self.assertEqual(move, (0, -1))

    def test_move_directions_keyerror(self):
        with self.assertRaises(Exception):
            MarsRoverInstructions.move_direction('NW')

    def test_left_spin(self):
        self.assertEqual(MarsRoverInstructions.left_spin('N'), 'W')
        self.assertEqual(MarsRoverInstructions.left_spin('W'), 'S')
        self.assertEqual(MarsRoverInstructions.left_spin('S'), 'E')
        self.assertEqual(MarsRoverInstructions.left_spin('E'), 'N')

    def test_left_spin_keyerror(self):
        with self.assertRaises(Exception):
            MarsRoverInstructions.left_spin('NE')

    def test_right_spin(self):
        self.assertEqual(MarsRoverInstructions.right_spin('N'), 'E')
        self.assertEqual(MarsRoverInstructions.right_spin('E'), 'S')
        self.assertEqual(MarsRoverInstructions.right_spin('S'), 'W')
        self.assertEqual(MarsRoverInstructions.right_spin('W'), 'N')

    def test_right_spin_keyerror(self):
        with self.assertRaises(Exception):
            MarsRoverInstructions.right_spin('SW')
