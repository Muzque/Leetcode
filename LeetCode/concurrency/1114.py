"""
1114. Print in Order
"""
"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. 
Thread A will call first(), thread B will call second(), and thread C will call 
third(). Design a mechanism and modify the program to ensure that second() is 
executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even 
though the numbers in the input seem to imply the ordering. The input format 
you see is mainly to ensure our tests' comprehensiveness.

 

Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input 
[1,2,3] means thread A calls first(), thread B calls second(), and thread C 
calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls 
third(), and thread C calls second(). "firstsecondthird" is the correct output.
"""
testcases = {
    '1': ([[1, 2, 3]], "firstsecondthird"),
    '2': ([[1, 3, 2]], "firstsecondthird"),
}

"""
Runtime: 56 ms, faster than 28.75% of Python3 online submissions 
Memory Usage: 14.8 MB, less than 30.37% of Python3 online submissions
"""

import threading


class Foo1:
    def __init__(self):
        self.locker1 = threading.Lock()
        self.locker1.acquire()
        self.locker2 = threading.Lock()
        self.locker2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.locker1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.locker1.acquire()
        printSecond()
        self.locker2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.locker2.acquire()
        printThird()


"""
Runtime: 80 ms, faster than 24.27% of Python3 online submissions
Memory Usage: 14.6 MB, less than 66.12% of Python3 online submissions
"""


class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.event1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        printThird()
