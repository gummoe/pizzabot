import sys
import re

from grid import Grid
from address import Address


def main():
    # Get STDIN args
    args = sys.argv

    # Build grid from args
    grid = parse_grid_arg(str(args[1]))

    # Build addresses from args
    address_args = args[2:]
    addresses = []
    for address_arg in address_args:
        addresses.append(parse_address_arg(address_arg, grid))

    # TODO: make this happen! folks need pizza!
    calculate_route(addresses, grid)



def parse_grid_arg(grid_arg):
    """
    Parses the argument for the grid size. Runs validation checks on
    arg format and ensures that grid size arguments are positive integers.

    :param grid_arg: string representation of grid size
    :return: Grid
    """
    pattern = re.compile('^[0-9]*x[0-9]*$')
    if not pattern.match(grid_arg):
        raise Exception("Grid size must be declared matching format 5x5")

    # Split on the 'x' and grab x and y size
    grid_arg_array = grid_arg.split('x')
    x = int(grid_arg_array[0])
    y = int(grid_arg_array[1])

    if x < 1 or y < 1:
        raise Exception("Grid size must be declared using positive numbers")

    return Grid(x, y)


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
        raise Exception(
            "Address coordinates must be declared matching format 1,3"
        )

    # Split on the 'x' and grab x and y size
    address_arg_array = address_arg.split(',')
    x = int(address_arg_array[0])
    y = int(address_arg_array[1])

    if x > grid.x or y > grid.y:
        raise Exception("Address coordinates must fit on grid")

    return Address(x, y)


def calculate_route(addresses, grid):
    pass


if __name__ == "__main__":
    main()
