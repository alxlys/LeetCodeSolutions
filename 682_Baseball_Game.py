# https://leetcode.com/problems/baseball-game/
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:

            try:
                stack.append(int(op))
            except Exception:
                if op == 'C':
                    stack.pop()
                elif op == 'D':
                    stack.append(stack[len(stack) - 1] * 2)
                elif op == '+':
                    length = len(stack)
                    stack.append(stack[length - 1] + stack[length - 2])

        return sum(stack)

    # Best solution
    # def calPoints(self, operations: List[str]) -> int:
    #     stack = []
    #
    #     for c in operations:
    #         if c == "C":
    #             stack.pop()
    #         elif c == "D":
    #             stack.append(stack[-1] * 2)
    #         elif c == "+":
    #             stack.append(stack[-1] + stack[-2])
    #         else:
    #             stack.append(int(c))
    #     return sum(stack)


if __name__ == '__main__':
    solution = Solution()

    ops = ["5", "2", "C", "D", "+"]
    print(solution.calPoints(ops))
    # Output: 30

    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(solution.calPoints(ops))
    # Output: 27

    ops = ["1", "C"]
    print(solution.calPoints(ops))
    # Output: 0
