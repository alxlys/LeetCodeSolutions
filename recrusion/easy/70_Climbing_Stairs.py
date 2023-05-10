# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()
        return self.__climb_stairs(0, n, memo)

    def __climb_stairs(self, curr_sum: int, n: int, memo: dict) -> int:
        if curr_sum == n:
            return 1
        elif curr_sum > n:
            return 0
        elif memo.get(curr_sum):
            return memo.get(curr_sum)
        else:
            step_one = curr_sum + 1
            step_one_res = memo.get(step_one)
            if not step_one_res:
                step_one_res = self.__climb_stairs(step_one, n, memo)
                memo[step_one] = step_one_res

            step_two = curr_sum + 2
            step_two_res = memo.get(step_two)
            if not step_two_res:
                step_two_res = self.__climb_stairs(step_two, n, memo)
                memo[step_two] = step_two_res

            return step_one_res + step_two_res

    def climb_stairs(self, n: int) -> int:
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
    print(solution.climb_stairs(2))

    # Output: 3
    print(solution.climbStairs(3))
    print(solution.climb_stairs(3))

    print(solution.climbStairs(38))
    print(solution.climb_stairs(38))
