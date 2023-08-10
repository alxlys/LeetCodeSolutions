import heapq
import math
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        res = []
        local_max = -math.inf

        def add_to_map(i):
            if nums[i] in num_count:
                num_count[nums[i]] = num_count[nums[i]] + 1
            else:
                num_count[nums[i]] = 1

        def remove_from_map(i):
            if nums[i] in num_count:
                count = num_count[nums[i]]
                count -= 1
                if count <= 0:
                    del num_count[nums[i]]

        l, r = 0, 0

        while r < len(nums):
            add_to_map(r)
            local_max = max(local_max, nums[r])
            if r == k - 1:
                res.append(local_max)
            if r < k:
                r += 1
                continue

            remove_from_map(l)
            l += 1
            r += 1
            res.append(max(num_count.keys()))

        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    # Output: [3, 3, 5, 5, 6, 7]
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

    # Input: nums = [1], k = 1
    # Output: [1]
    print(solution.maxSlidingWindow([1], 1))
