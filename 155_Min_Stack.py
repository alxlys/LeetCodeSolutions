class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == '__main__':
    minStack = MinStack()

    # case2
    minStack.push(0)
    minStack.push(1)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())

    # case0
    # minStack.push(-1)
    # print(minStack.top())
    # print(minStack.getMin())

    # case1
    # minStack.push(-2)
    # minStack.push(0)
    # minStack.push(-3)
    # print(minStack.getMin())  # // return -3
    # minStack.pop()
    # print(minStack.top())  # // return 0
    # print(minStack.getMin())  # // return -2
