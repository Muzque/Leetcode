import time
import importlib
import argparse

TestSets = {
    '2021-05-07': 'minDistance',
    '2021-05-08': 'superpalindromesInRange',
    '2021-05-09': 'isPossible',
}


def select_problem(category: str, filename: str):
    mod = importlib.import_module(f'{category}.{filename}')
    solution = getattr(mod, 'Solution')
    testcases = getattr(mod, 'testcases')
    return solution, testcases


def examine(cls, method: str, testcases: dict) -> None:
    sol = cls()
    cost = 0
    for idx, testcase in testcases.items():
        print(f'Question {idx}\n')
        inputs, ans = testcase
        print(f'Inputs: {inputs}')
        t0 = time.time()
        ret = getattr(sol, method)(*inputs)
        dt = (time.time() - t0) * 1000
        cost += dt
        print(f'Cost: {dt} ms')
        if ret != ans:
            print('------------------------------')
            print(
                f'*WrongAnswer index {idx}\n'
                f'answer: {ans}\n'
                f'yours: {ret}\n'
            )
            break
        print('PASS')
    else:
        n_cases = len(testcases)
        print(
            f'------------------------------\n'
            f'Accepted\n'
            f'Total cases: {n_cases}\n'
            f'Avg. cost : {cost/n_cases} ms\n'
        )


def main(args):
    category = 'python3'
    filename = args.solution
    solution, testcases = select_problem(category, filename)
    method = TestSets[filename]
    examine(
        cls=solution,
        method=method,
        testcases=testcases,
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
    main(parser.parse_args())
