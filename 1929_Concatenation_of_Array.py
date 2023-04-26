# https://leetcode.com/problems/concatenation-of-array/
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 1]
    print(solution.getConcatenation(nums))
    # Output: [1,2,1,1,2,1]

    nums = [1, 3, 2, 1]
    print(solution.getConcatenation(nums))
    # Output: [1,3,2,1,1,3,2,1]
