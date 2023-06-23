# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            min_height = min(height[l], height[r])
            max_area = max(max_area, min_height * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == '__main__':
    solution = Solution()

    # Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Output: 49
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    # Input: height = [1, 1]
    # Output: 1
    print(solution.maxArea([1, 1]))
