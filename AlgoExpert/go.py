import os
import time
import importlib
import argparse


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f"> {(te - ts) * 1000} ms")
        return result

    return timed


class Runner:
    def __init__(self, question: str):
        self.question = question.rstrip('.py')
        self.func = self.load()

    def load(self):
        module_path = '.'.join(self.question.split(os.sep))
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
        help="select question",
        dest="question",
        required=True,
    )
    main(parser.parse_args())
