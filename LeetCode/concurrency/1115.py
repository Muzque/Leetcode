"""
1115. Print FooBar Alternately
https://leetcode.com/problems/print-foobar-alternately/
"""
"""
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads. Thread A 
will call foo() while thread B will call bar(). Modify the given program to 
output "foobar" n times.

 

Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them 
calls foo(), while the other calls bar(). "foobar" is being output 1 time.

Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""
testcases = {
    '1': ([1], 'foobar'),
    '2': ([2], 'foobarfoobar'),
}

"""
Runtime: 36 ms, faster than 91.90% of Python3 online submissions 
Memory Usage: 14.7 MB, less than 42.17% of Python3 online submissions
"""
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.tl1 = threading.Lock()
        self.tl2 = threading.Lock()
        self.tl1.acquire()
        self.tl2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.tl2.release()
            self.tl1.acquire()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.tl2.acquire()
            printBar()
            self.tl1.release()
