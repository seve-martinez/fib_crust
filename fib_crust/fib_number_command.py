import argparse

from .fib_crust import fibonacci_number


def fib_number_command() -> None:
    parser = argparse.ArgumentParser(description='Calculate fib numbs')

    parser.add_argument('--number', action='store', type=int, required=True)

    args = parser.parse_args()
    print(f"Your fib number is: {fibonacci_number(n=args.number)}")
