# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 3, 1]
    # Output: true
    print(solution.containsDuplicate([1, 2, 3, 1]))

    # Input: nums = [1, 2, 3, 4]
    # Output: false
    print(solution.containsDuplicate([1, 2, 3, 4]))

    # Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    # Output: true
    print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
