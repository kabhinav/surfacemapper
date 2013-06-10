import unittest

from pkg_resources import resource_string

class TestSurfaceMapper(unittest.TestCase):

    def setUp(self):
        from surfacemapper.mapper import Mapper

        self.mapper = Mapper()

    def tearDown(self):
        self.mapper = None

    def test_mars_surface_mapper(self):
        user_input = resource_string('surfacemapper.data', 'input.txt')
        self.mapper.parse_input(user_input)
        self.mapper.delegate()
        result = self.mapper.final_locations()
        expected = '1 3 N\n5 1 E\n'

        self.assertEqual(result, expected)
