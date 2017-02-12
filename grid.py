from address import Address


class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.addresses = []

    def calculate_route(self):
        """
        Calculates the route to visit all of the addresses on the grid,
        assuming starting position coordinates of (0, 0).

        :return: String
        """
        if not self.addresses:
            return None

        # Get directions from starting coordinates (0, 0) to first address
        directions = self.calculate_route_between_addresses(
            Address(0, 0),
            self.addresses[0]
        )

        # Get directions for remaining addresses
        for i in range(len(self.addresses) - 1):
            addr_directions = self.calculate_route_between_addresses(
                self.addresses[i],
                self.addresses[i+1]
            )
            directions += addr_directions

        return directions

    @staticmethod
    def calculate_route_between_addresses(address1, address2):
        """
        Generates a string representation of the route to take between
        two addresses using capital letters to represent cardinal direction
        steps. For example, 'NNN' = go North three times.

        Calculation for routes is performed using simple mathematical
        differences between address coordinates and than translating that
        difference into the appropriate number of cardinal number characters.

        :param address1: Address
        :param address2: Address
        :return: String
        """
        x_difference = address2.x - address1.x
        y_difference = address2.y - address1.y

        x_steps = [
            'E' if x_difference > 0 else 'W' for _ in range(abs(x_difference))
        ]
        y_steps = [
            'N' if y_difference > 0 else 'S' for _ in range(abs(y_difference))
        ]

        directions = x_steps + y_steps
        if directions:
            return ''.join(directions) + 'D'
        else:
            return 'D'
