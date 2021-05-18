import time
import importlib
import argparse
from typing import Optional

KEY_DAILY = 'daily'
KEY_WEEKLY = 'weekly'
KEY_SOLUTION = 'Solution'
KEY_TESTCASE = 'testcases'
TEST_TIMES = 10


def select_problem(category: str, filename: str):
    mod = importlib.import_module(f'{category}.{filename}')
    solution = getattr(mod, KEY_SOLUTION)()
    testcases = getattr(mod, KEY_TESTCASE)
    return solution, testcases


def find_method(solution) -> str:
    for m in dir(solution):
        if not m.startswith('_'):
            return m


class Examine:
    def __init__(self, sol, method: str, testcases: dict, options: dict):
        self.sol = sol
        self.method = method
        self.testcases = testcases
        self.options = options

    def print(self, sentence, force=False):
        if not self.options['silence'] or force:
            print(sentence)

    def return_wrong(self, index: int, answer, yours):
        print(
            f'------------------------------\n'
            f'*WrongAnswer index {index}\n'
            f'answer: {answer}\n'
            f'yours: {yours}\n'
        )

    def return_pass(self):
        self.print('PASS\n')

    def return_accept(self, cost: float, n_cases: int):
        self.print(
            f'------------------------------\n'
            f'Accepted\n'
            f'Total cases: {n_cases}\n'
            f'Case avg. cost : {cost / n_cases} ms\n'
        )

    def return_average_cost(self, loop: int, costs: float):
        avg_cost = costs / loop
        self.print(
            f'------------------------------\n'
            f'Loop: {loop}\n'
            f'Loop avg. cost: {avg_cost} ms\n',
            force=True
        )

    def init_test(self, index: int, testcase):
        self.print(f'Question {index}')
        inputs, ans = testcase
        if not self.options['hide_inputs']:
            self.print(f'Inputs: {inputs}')
        return index, inputs, ans

    def run_test(self, inputs):
        t0 = time.time()
        ret = getattr(self.sol, self.method)(*inputs)
        dt = (time.time() - t0) * 1000
        self.print(f'Cost: {dt} ms')
        return dt, ret

    def check_result(self, index: int, answer, yours) -> bool:
        if yours != answer:
            self.return_wrong(index, answer, yours)
            return False
        self.return_pass()
        return True

    def get_testcase(self):
        if self.options['case'] is None:
            return self.testcases, len(self.testcases)
        index = self.options['case']
        testcases = {
            index: self.testcases[index],
        }
        return testcases, 1

    def go(self) -> Optional[float]:
        cost = 0
        testcases, n_cases = self.get_testcase()
        for idx, testcase in testcases.items():
            idx, inputs, ans = self.init_test(idx, testcase)
            dt, ret = self.run_test(inputs)
            cost += dt
            ok = self.check_result(idx, ans, ret)
            if not ok:
                return None
        else:
            self.return_accept(cost, n_cases)
        return cost

    def go_loop(self, loop: int):
        total_cost = 0
        for i in range(loop):
            cost = self.go()
            if cost is None:
                return
            total_cost += cost
        self.return_average_cost(loop, total_cost)


def main(args):
    if args.weekly:
        week, filename = args.weekly.split('.')
        category = f'{KEY_WEEKLY}.{week}'
    elif args.daily:
        category = KEY_DAILY
        filename = args.daily
    else:
        raise Exception('Must be daily or weekly')
    solution, testcases = select_problem(category, filename)
    method = find_method(solution)
    loop = TEST_TIMES if args.avg else 1
    runner = Examine(
        sol=solution,
        method=method,
        testcases=testcases,
        options={
            'hide_inputs': args.hide_inputs,
            'silence': loop > 1,
            'case': args.case,
        },
    )
    runner.go_loop(loop)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Examine your solution")
    parser.add_argument(
        "-d",
        "--daily",
        type=str,
        help="select daily problem",
        required=False,
    )
    parser.add_argument(
        "-hi",
        "--hide_inputs",
        help="hide inputs",
        action="store_true",
    )
    parser.add_argument(
        "-a",
        "--avg",
        help="test multiple times to get average runtime cost",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--case",
        type=str,
        help="select one case to test by index",
        required=False,
    )
    parser.add_argument(
        "-w",
        "--weekly",
        type=str,
        help="select problem number of weekly contest",
        required=False,
    )
    main(parser.parse_args())
