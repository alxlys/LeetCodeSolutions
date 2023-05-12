# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        self.__quick_sort_Kth__(nums, 0, len(nums) - 1, k)
        return nums[k]

    def __quick_sort_Kth__(self, nums: List[int], s: int, e: int, k: int) -> None:
        if e - s + 1 <= 1:
            return

        pivot = nums[e]
        left = s

        for i in range(s, e):
            if nums[i] < pivot:
                tmp = nums[i]
                nums[i] = nums[left]
                nums[left] = tmp
                left += 1

        nums[e] = nums[left]
        nums[left] = pivot

        if left == k:
            return
        elif k < left:
            self.__quick_sort_Kth__(nums, s, left - 1, k)
        else:
            self.__quick_sort_Kth__(nums, left + 1, e, k)


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    # Output: 5

    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))

    # Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
    # Output: 4

    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

    # [3, 1, 2, 4]
    # Output: 3

    print(solution.findKthLargest([3, 1, 2, 4], 2))

