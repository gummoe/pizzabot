import sys
import re

from grid import Grid
from address import Address


def main():
    # Get command line args
    args = sys.argv

    # Build grid from args
    grid = parse_grid_arg(args[1])

    # Build addresses from args
    for address_arg in args[2:]:
        parse_address_arg(address_arg, grid)

    # Calculate and display route
    print grid.calculate_route()


def parse_grid_arg(grid_arg):
    """
    Parses the argument for the grid size. Runs validation checks on
    arg format and ensures that grid size arguments are positive integers.

    :param grid_arg: string representation of grid size
    :return: Grid
    """
    pattern = re.compile('^[0-9]*x[0-9]*$')
    if not pattern.match(grid_arg):
        raise ValueError("Grid size must be declared matching format 5x5")

    # Split on the 'x' and grab x and y size
    grid_arg_array = grid_arg.split('x')
    width = int(grid_arg_array[0])
    height = int(grid_arg_array[1])

    # Dimensions must be positive
    if width < 1 or height < 1:
        raise ValueError("Grid size must be declared using positive numbers")

    # Switch to width and height!
    return Grid(width, height)


def parse_address_arg(address_arg, grid):
    """
    Parses an argument for a delivery address. Runs validation checks on
    arg format and ensures that the address will fit on the grid.

    :param address_arg: string representation of address coordinates
    :param grid: Grid
    :return: Address
    """
    pattern = re.compile('^[0-9]*,[0-9]*$')
    if not pattern.match(address_arg):
        raise ValueError(
            "Address coordinates must be declared matching format 1,3"
        )

    # Split on the ',' and grab x and y coordinates
    address_arg_array = address_arg.split(',')
    x = int(address_arg_array[0])
    y = int(address_arg_array[1])

    # Coordinates must fit on grid
    if x > grid.width or y > grid.height:
        raise ValueError("Address coordinates must fit on grid")

    # Create new Address object and add to grid
    address = Address(x, y)
    grid.addresses.append(address)


if __name__ == "__main__":
    main()
