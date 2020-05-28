class StockSpanner:

    def __init__(self):
        self.idx = -1
        self.max = -1
        self.arr = []

    def next(self, price: int) -> int:
        self.idx += 1
        if not self.arr:
            self.max = self.idx
            count = 1
        elif price >= self.arr[self.max]:
            self.max = self.idx
            count = len(self.arr) + 1
        else:
            count = 1
            for num in self.arr[::-1]:
                if num <= price:
                    count += 1
                else:
                    break
        self.arr.append(price)
        return count
