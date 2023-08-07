# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1
            i -= 1

        while m > 0:
            nums1[i] = nums1[m - 1]
            m -= 1
            i -= 1

        while n > 0:
            nums1[i] = nums2[n - 1]
            n -= 1
            i -= 1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    # Output: [1, 2, 2, 3, 5, 6]
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)

    # Input: nums1 = [1], m = 1, nums2 = [], n = 0
    # Output: [1]
    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    print(nums1)

    # Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    # Output: [1]
    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    print(nums1)
