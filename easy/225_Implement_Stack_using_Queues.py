# https://leetcode.com/problems/implement-stack-using-queues/
import queue


class MyStack:

    def __init__(self):
        self.q = queue.Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        for i in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        return self.q.get()

    def top(self) -> int:
        for i in range(self.q.qsize() - 1):
            self.q.put(self.q.get())
        res = self.q.get()
        self.q.put(res)
        return res

    def empty(self) -> bool:
        return self.q.empty()


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top())  # return 2
    print(myStack.pop())  # return 2
    print(myStack.empty())  # return False
