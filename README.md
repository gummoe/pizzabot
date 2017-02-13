# pizzabot
Route finder for grid points... for pizza

## Running the program
Pizzabot is designed to be run from the command-line. To run it, navigate to the `pizzabot` directory and enter something like:

`python pizzabot.py 5x5 1,3 2,2 4,4`

The first argument is the size of the grid and must match the format: `9x9`

All additional arguments afterward are coordinates that must fit on the grid. The formatting of each coordinate argument *must* match: `1,3`

## Tests
To run the tests, navigate to the `pizzabot` directory in the command-line and enter: `python tests.py` or `python tests.py -v` for more verbose output. 
