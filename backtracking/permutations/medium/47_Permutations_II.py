# https://leetcode.com/problems/permutations-ii/
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # TODO NOT WORKING PROPERLY
        perms = [[]]
        for n in nums:
            next_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    next_perms.append(p_copy)
            perms = next_perms
        return perms


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 1, 2]
    # Output:
    # [[1, 1, 2],
    #  [1, 2, 1],
    #  [2, 1, 1]]
    print(solution.permuteUnique([1, 1, 2]))

    # Input: nums = [1, 2, 3]
    # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(solution.permuteUnique([1, 2, 3]))
