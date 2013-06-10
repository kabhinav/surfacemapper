import unittest
import mock


ROVER_ID = 1


class TestMapper(unittest.TestCase):

    def setUp(self):
        from surfacemapper.mapper import Mapper
        self.mapper = Mapper()

    def testDown(self):
        self.mapper = None

    def test_mapper_init(self):
        self.assertIsNotNone(self.mapper)
        self.assertIsNone(self.mapper.controller)
        self.assertEqual(self.mapper.rovers, [])

    def test_parse_input(self):
        from surfacemapper.mars_rover_controller import MarsRoverController
        from surfacemapper.rover import Rover

        user_input = '5 5\n1 2 N\nLm'
        self.mapper.parse_input(user_input)
        self.assertIsNotNone(self.mapper.controller)
        self.assertIsInstance(self.mapper.controller, MarsRoverController)
        self.assertEqual(self.mapper.controller.grid_origin, (0, 0))
        self.assertEqual(self.mapper.controller.grid_end, (5, 5))
        self.assertEqual(len(self.mapper.rovers), 1)

        rover = self.mapper.rovers[0]
        self.assertIsInstance(rover, Rover)
        self.assertEqual(rover.id, ROVER_ID)
        self.assertEqual(rover.position, (1, 2, 'N'))
        self.assertEqual(rover.instructions, ['L', 'M'])

    def test_parse_grid_endpoint_exception(self):
        with self.assertRaises(ValueError):
            self.mapper.parse_grid_endpoint('5 v')

    def test_parse_rover_value_error(self):
        with self.assertRaises(ValueError):
            self.mapper.parse_rover(ROVER_ID, ['N 2 N'])

    def test_parse_rover_exception(self):
        with self.assertRaises(Exception):
            self.mapper.parse_rover(ROVER_ID, ['2 N'])

    @mock.patch('surfacemapper.mapper.Mapper.move')
    @mock.patch('surfacemapper.mapper.Mapper.turn_right')
    @mock.patch('surfacemapper.mapper.Mapper.turn_left')
    def test_delegate(self, m_left, m_right, m_move):
        from surfacemapper.rover import Rover
        rover = Rover(ROVER_ID, (1, 2, 'N'), ['L', 'R', 'M'])
        self.mapper.rovers.append(rover)

        self.mapper.delegate()
        m_left.assert_called_once_with(rover)
        m_right.assert_called_once_with(rover)
        m_move.assert_called_once_with(rover)

    @mock.patch('surfacemapper.mapper.Mapper.turn_right')
    @mock.patch('surfacemapper.mapper.Mapper.turn_left')
    def test_delegate_exception(self, m_left, m_right):
        from surfacemapper.rover import Rover
        self.mapper.rovers = []
        rover = Rover(ROVER_ID, (1, 2, 'N'), ['L', 'R', 'W'])
        self.mapper.rovers.append(rover)

        with self.assertRaises(Exception):
            self.mapper.delegate()

    @mock.patch('surfacemapper.mapper.MarsRoverController.turn')
    def test_turn_left(self, m_turn):
        from surfacemapper.rover import Rover
        from surfacemapper.mars_rover_controller import MarsRoverController

        rover = Rover(ROVER_ID, (1, 2, 'N'), ['L', 'R', 'M'])
        self.mapper.controller = MarsRoverController((0, 0), (5, 5))

        self.mapper.turn_left(rover)
        m_turn.assert_called_once_with(ROVER_ID, 'W')

    @mock.patch('surfacemapper.mapper.MarsRoverController.turn')
    def test_turn_right(self, m_turn):
        from surfacemapper.rover import Rover
        from surfacemapper.mars_rover_controller import MarsRoverController

        rover = Rover(ROVER_ID, (1, 2, 'N'), ['L', 'R', 'M'])
        self.mapper.controller = MarsRoverController((0, 0), (5, 5))

        self.mapper.turn_right(rover)
        m_turn.assert_called_once_with(ROVER_ID, 'E')

    @mock.patch('surfacemapper.mapper.MarsRoverController.move')
    def test_move(self, m_move):
        from surfacemapper.rover import Rover
        from surfacemapper.mars_rover_controller import MarsRoverController

        rover = Rover(ROVER_ID, (1, 2, 'N'), ['L', 'R', 'M'])
        self.mapper.controller = MarsRoverController((0, 0), (5, 5))

        self.mapper.move(rover)
        m_move.assert_called_once_with(ROVER_ID, (0, 1))

    def test_final_locations(self):
        from surfacemapper.rover import Rover
        self.mapper.rovers.append(Rover(ROVER_ID, (1, 2, 'N'), ['L']))
        self.mapper.rovers.append(Rover(ROVER_ID, (4, 1, 'W'), ['R']))

        result = self.mapper.final_locations()
        expected = '1 2 N\n4 1 W\n'
        self.assertEqual(result, expected)

    @mock.patch('surfacemapper.mapper.Mapper')
    @mock.patch('surfacemapper.mapper.sys')
    def test_main_no_atty(self, m_sys, m_mapper):
        from surfacemapper.mapper import main
        m_sys.stdin.isatty.return_value = False
        m_sys.stdin.read.return_value = '1 2 N\n4 1 W\n'

        main()

        mapper = m_mapper.return_value
        mapper.parse_input.assert_called_once_with('1 2 N\n4 1 W')
        mapper.delegate.assert_called_once_with()
        mapper.final_locations.assert_called_once_with()
