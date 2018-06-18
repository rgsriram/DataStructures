class Node(object):
    def __init__(self, data, max, min):
        self.data = data
        self.max = max
        self.min = min


class MinMaxStack(object):
    def __init__(self):
        self.stack = []
        self._max = float("-inf")
        self._min = float("inf")

    def push(self, x):
        self._min = min(self._min, x)
        self._max = max(self._max, x)

        self.stack.append(Node(x, self._max, self._min))

    def pop(self):

        if not len(self.stack) <= 0:
            self.stack.pop()

        if len(self.stack) > 0:
            peek = self.peek()

            self._max = peek.max
            self._min = peek.min

        else:
            self._max = float("-inf")
            self._min = float("inf")

    def mini(self):
        return self._min

    def maxi(self):
        return self._max

    def peek(self):
        return self.stack[-1]


arr = [10, 5, 3, 20, 50, 9, 1]

m = MinMaxStack()
for each in arr:
    m.push(each)

print m.mini(), m.maxi()

m.pop()

print m.mini(), m.maxi()

m.pop()
print m.mini(), m.maxi()

m.pop()
print m.mini(), m.maxi()

m.pop()
print m.mini(), m.maxi()