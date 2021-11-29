"""

https://leetcode.com/problems/print-zero-even-odd/submissions/
"""
"""
Suppose you are given the following exercise:

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // constructor
  public void zero(printNumber) { ... }  // only output 0's
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A will call zero() which should only output 0's.
Thread B will call even() which should only ouput even numbers.
Thread C will call odd() which should only output odd numbers.
Each of the threads is given a printNumber method to output an integer. Modify 
the given program to output the series 010203040506... where the length of the 
series must be 2n.

 

Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them 
calls zero(), the other calls even(), and the last one calls odd(). "0102" is 
the correct output.

Example 2:

Input: n = 5
Output: "0102030405"
"""
testcases = {
    '1': ([2], '0102'),
}

"""
Runtime: 40 ms, faster than 69.87% of Python3 online submissions
Memory Usage: 15.6 MB, less than 36.54% of Python3 online submissions 
"""

import threading


class ZeroEvenOdd1:
    def __init__(self, n):
        self.n = n
        self.cnt = 1
        self.tl0 = threading.Lock()
        self.tl1 = threading.Lock()
        self.tl2 = threading.Lock()
        self.tl1.acquire()
        self.tl2.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.tl0.acquire()
            printNumber(0)
            if self.cnt % 2 == 1:
                self.tl1.release()
            else:
                self.tl2.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.tl2.acquire()
            printNumber(self.cnt)
            self.cnt += 1
            self.tl0.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.tl1.acquire()
            printNumber(self.cnt)
            self.cnt += 1
            self.tl0.release()


"""
Runtime: 72 ms, faster than 8.01% of Python3 online submissions 
Memory Usage: 15.3 MB, less than 89.42% of Python3 online submissions
"""


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cnt = 1
        self.te0 = threading.Event()
        self.te1 = threading.Event()
        self.te2 = threading.Event()
        self.te0.set()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.te0.wait()
            printNumber(0)
            self.te0.clear()
            if self.cnt % 2 == 1:
                self.te1.set()
            else:
                self.te2.set()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.te2.wait()
            printNumber(self.cnt)
            self.te2.clear()
            self.cnt += 1
            self.te0.set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.te1.wait()
            printNumber(self.cnt)
            self.te1.clear()
            self.cnt += 1
            self.te0.set()
