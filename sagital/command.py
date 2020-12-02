from argparse import ArgumentParser
from .sagital_brain import run_averages
import sys


def process():

    parser = ArgumentParser(description="Weighted mean of squared numbers")
    # parser.add_argument("numbers", nargs='+', help="the list of numbers")
    parser.add_argument("numbers", type=int, nargs='+', help="the list of numbers")
    parser.add_argument("--weights", "-w", type=int, nargs='+', help="the list of weights")
    arguments = parser.parse_args()

    # numbers = convert_numbers(arguments.numbers)
    numbers = arguments.numbers
    if arguments.weights:
        weights = arguments.weights
    else:
        weights = [1] * len(numbers)

    run_averages(numbers, weights)

if __name__ == "__main__":
    process()