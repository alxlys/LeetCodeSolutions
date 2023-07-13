# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        one, two = 1, 1
        for i in range(2, n + 1):
            temp = one
            one = one + two
            two = temp
        return one


if __name__ == '__main__':
    solution = Solution()

    # Output: 2
    print(solution.climbStairs(2))

    # Output: 3
    print(solution.climbStairs(3))

    print(solution.climbStairs(38))
