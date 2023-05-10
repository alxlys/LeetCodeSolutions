# https://leetcode.com/problems/sort-an-array/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.__merge_sort__(nums, 0, len(nums) - 1)

    def __merge_sort__(self, arr: List[int], s: int, e: int) -> List[int]:
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2
        self.__merge_sort__(arr, s, m)
        self.__merge_sort__(arr, m + 1, e)

        self.__merge__(arr, s, m, e)

        return arr

    def __merge__(self, arr: List[int], s: int, m: int, e: int):
        left = arr[s: m + 1]
        right = arr[m + 1: e + 1]

        i = 0
        j = 0
        k = s

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [5, 2, 3, 1]
    # Output: [1, 2, 3, 5]
    print(solution.sortArray([5, 2, 3, 1]))

    # Input: nums = [5, 1, 1, 2, 0, 0]
    # Output: [0, 0, 1, 1, 2, 5]
    print(solution.sortArray([5, 1, 1, 2, 0, 0]))
