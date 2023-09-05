# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from typing import List


class Solution:
    # O(n*log n)
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        sorted_freq = []
        for item, freq in count_map.items():
            heapq.heappush(sorted_freq, [-1 * freq, item])

        res = []
        while True:
            rec = heapq.heappop(sorted_freq)
            res.append(rec[1])
            if len(res) == k:
                break

        return res

    # O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        for item, frequency in count_map.items():
            freq[frequency].append(item)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    # Output: [1, 2]
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))

    # Input: nums = [1], k = 1
    # Output: [1]
    print(solution.topKFrequent([1], 1))
