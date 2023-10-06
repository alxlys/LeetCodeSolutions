# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                res = op1 + op2
                stack.append(res)
            elif op == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                res = op1 - op2
                stack.append(res)
            elif op == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                res = op1 * op2
                stack.append(res)
            elif op == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                res = op1 / op2
                stack.append(int(res))
            else:
                res = int(op)
                stack.append(res)

        return stack[0]


if __name__ == '__main__':
    solution = Solution()

    # Input: tokens = ["2", "1", "+", "3", "*"]
    # Output: 9
    # Explanation: ((2 + 1) * 3) = 9
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))

    # Input: tokens = ["4", "13", "5", "/", "+"]
    # Output: 6
    # Explanation: (4 + (13 / 5)) = 6
    print(solution.evalRPN(["4", "13", "5", "/", "+"]))

    # Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # Output: 22
    # Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
