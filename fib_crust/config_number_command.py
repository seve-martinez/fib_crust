import argparse
import yaml
import os

from pprint import pprint

from .fib_crust import run_config


def config_number_command() -> None:
    parser = argparse.ArgumentParser(description='Calc fibs w a config')
    parser.add_argument('--path', action='store', type=str, required=True)
    args = parser.parse_args()

    with open(str(os.getcwd()) + '/' + args.path) as f:
        config_data: dict = yaml.load(f)

    print(f"Here is the config data: {config_data}")
    print(f"And the result: {run_config(config_data)}")
