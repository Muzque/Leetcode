import os
import importlib
import argparse


class Runner:
    def __init__(self, question: str):
        self.question = question.rstrip('.py')
        self.func = self.load()

    def load(self):
        module_path = '.'.join(self.question.split(os.sep))
        mod = importlib.import_module(module_path)
        return getattr(mod, 'main')

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
        help="select question",
        dest="question",
        required=True,
    )
    main(parser.parse_args())
