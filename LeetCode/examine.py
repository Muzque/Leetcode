import time
import importlib
import argparse

KEY_CATEGORY = 'python3'
KEY_SOLUTION = 'Solution'
KEY_TESTCASE = 'testcases'


def select_problem(category: str, filename: str):
    mod = importlib.import_module(f'{category}.{filename}')
    solution = getattr(mod, KEY_SOLUTION)()
    testcases = getattr(mod, KEY_TESTCASE)
    return solution, testcases


def find_method(solution) -> str:
    for m in dir(solution):
        if not m.startswith('_'):
            return m


def examine(sol, method: str, testcases: dict, options: dict) -> None:
    cost = 0
    for idx, testcase in testcases.items():
        print(f'Question {idx}')
        inputs, ans = testcase
        if not options['hide_inputs']:
            print(f'Inputs: {inputs}')
        t0 = time.time()
        ret = getattr(sol, method)(*inputs)
        dt = (time.time() - t0) * 1000
        cost += dt
        print(f'Cost: {dt} ms')
        if ret != ans:
            print(
                f'------------------------------\n'
                f'*WrongAnswer index {idx}\n'
                f'answer: {ans}\n'
                f'yours: {ret}\n'
            )
            break
        print('PASS\n')
    else:
        n_cases = len(testcases)
        print(
            f'------------------------------\n'
            f'Accepted\n'
            f'Total cases: {n_cases}\n'
            f'Avg. cost : {cost/n_cases} ms\n'
        )


def main(args):
    filename = args.solution
    solution, testcases = select_problem(KEY_CATEGORY, filename)
    method = find_method(solution)
    examine(
        sol=solution,
        method=method,
        testcases=testcases,
        options={
            'hide_inputs': args.hide_inputs,
        },
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Examine your solution")
    parser.add_argument(
        "-s",
        "--solution",
        type=str,
        help="select solutions",
        required=True,
    )
    parser.add_argument(
        "-hi",
        "--hide_inputs",
        help="hide inputs",
        action="store_true",
    )
    main(parser.parse_args())
