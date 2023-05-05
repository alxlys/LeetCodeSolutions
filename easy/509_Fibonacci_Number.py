# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    solution = Solution()
    # Input: n = 2
    # Output: 1
    # Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    print(solution.fib(2))

    # Input: n = 3
    # Output: 2
    # Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    print(solution.fib(3))

    # Input: n = 4
    # Output: 3
    # Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    print(solution.fib(4))
