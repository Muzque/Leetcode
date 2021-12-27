import importlib
import argparse
from lib import timeit


class Runner:
    def __init__(self, question: str):
        self.question = question.rstrip('.py')
        self.func = self.load()

    def load(self):
        module_path = f'problems.{self.question}'
        mod = importlib.import_module(module_path)
        return getattr(mod, 'main')

    @timeit
    def go(self):
        self.func()


def main(args):
    r = Runner(args.question)
    r.go()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test")
    parser.add_argument(
        "-q",
        "--question",
        type=str,
        help="select question under problems directory",
        dest="question",
        required=True,
    )
    main(parser.parse_args())
