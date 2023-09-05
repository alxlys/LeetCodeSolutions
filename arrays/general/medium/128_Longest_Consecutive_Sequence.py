# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            # start of the sequence
            if (num - 1) not in nums_set:
                curr_len = 1
                while (num + curr_len) in nums_set:
                    curr_len += 1
                max_len = max(curr_len, max_len)

        return max_len


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [100, 4, 200, 1, 3, 2]
    # Output: 4
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))

    # Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    # Output: 9
    print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
