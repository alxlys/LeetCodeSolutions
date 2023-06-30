# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = None
        for i in range(k):
            res = heapq.heappop(nums)
        return -res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    # Output: 5
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))

    # Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
    # Output: 4
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
