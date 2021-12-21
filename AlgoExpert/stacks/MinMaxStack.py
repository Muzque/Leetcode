# Feel free to add new properties and methods to the class.
"""
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.max = float('-inf')

    def _update_min(self, num, drop=False):
        if drop and num == self.min:
            self.min = min(self.stack or [float('inf')])
        elif not drop and num < self.min:
            self.min = num

    def _update_max(self, num, drop=False):
        if drop and num == self.max:
            self.max = max(self.stack or [float('-inf')])
        elif not drop and num > self.max:
            self.max = num

    def peek(self):
        return self.stack[-1]

    def pop(self):
        num = self.stack.pop()
        self._update_min(num, True)
        self._update_max(num, True)
        return num

    def push(self, number):
        self.stack.append(number)
        self._update_min(number)
        self._update_max(number)

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max
"""


# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.cached = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.cached.pop()
        return self.stack.pop()

    def push(self, number):
        cache = {'min': number, 'max': number}
        if len(self.stack):
            latest = self.cached[-1]
            cache['min'] = min(number, latest['min'])
            cache['max'] = max(number, latest['max'])
        self.cached.append(cache)
        self.stack.append(number)

    def getMin(self):
        return self.cached[-1]['min']

    def getMax(self):
        return self.cached[-1]['max']
