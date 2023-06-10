# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count


if __name__ == '__main__':
    solution = Solution()

    # Input: n = 00000000000000000000000000001011
    # Output: 3
    print(solution.hammingWeight(1011))

    # Input: n = 00000000000000000000000010000000
    # Output: 1
    print(solution.hammingWeight(10000000))

    # Input: n = 11111111111111111111111111111101
    # Output: 31
    print(solution.hammingWeight(11111111111111111111111111111101))



