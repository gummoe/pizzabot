import unittest
from grid import Grid
from address import Address
from pizzabot import (
    parse_address_arg,
    parse_grid_arg
)


class ArgParsingTest(unittest.TestCase):

    def test_grid_arg_parsing(self):
        # Base test object
        grid = Grid(5, 5)

        # Test argument grid equals matching base test object
        arg_grid = parse_grid_arg('5x5')
        self.assertEquals(grid.height, arg_grid.height)
        self.assertEquals(grid.width, arg_grid.width)

        # Test failure for incorrect formatting
        with self.assertRaises(ValueError):
            parse_grid_arg('5x')

        # Test failure for invalid grid size
        with self.assertRaises(ValueError):
            parse_grid_arg('0x0')

    def test_address_arg_parsing(self):
        # Base test objects
        grid = Grid(5, 5)
        address = Address(1, 3)

        # Test argument address equals matching base test object
        parse_address_arg('1,3', grid)
        self.assertEquals(address.x, grid.addresses[0].x)
        self.assertEquals(address.y, grid.addresses[0].y)

        # Test failure for incorrect formatting
        with self.assertRaises(ValueError):
            parse_address_arg('3, 4', grid)

        # Test failure for negative coordinates
        with self.assertRaises(ValueError):
            parse_address_arg('-1,-1', grid)

        # Test for failure of coordinates larger than grid
        with self.assertRaises(ValueError):
            parse_address_arg('6,6', grid)


class GridTest(unittest.TestCase):

    def test_address_router(self):
        # Base test objects
        grid = Grid(5, 5)
        address1 = Address(1, 3)
        address2 = Address(4, 4)
        grid.addresses.append(address1)
        grid.addresses.append(address2)

        # Test route between addresses successfully calculates
        route = grid.calculate_route_between_addresses(address1, address2)
        self.assertEquals(route, "EEEND")

    def test_full_route(self):
        # Base test objects
        grid = Grid(5, 5)
        address1 = Address(1, 3)
        address2 = Address(4, 4)
        grid.addresses.append(address1)
        grid.addresses.append(address2)

        route = grid.calculate_route()
        self.assertEquals(route, 'ENNNDEEEND')


if __name__ == '__main__':
    unittest.main()