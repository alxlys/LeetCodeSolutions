# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()
        window.add(nums[0])

        for right in range(1, len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 3, 1], k = 3
    # Output: true
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))

    # Input: nums = [1, 0, 1, 1], k = 1
    # Output: true
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))

    # Input: nums = [1, 2, 3, 1, 2, 3], k = 2
    # Output: false
    print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
