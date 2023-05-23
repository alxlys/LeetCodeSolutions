# https://leetcode.com/problems/last-stone-weight/
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            biggest = heapq.heappop(stones)
            if stones:
                biggest = biggest - heapq.heappop(stones)
                if biggest != 0:
                    heapq.heappush(stones, biggest)
        return -stones[0] if stones else 0


if __name__ == '__main__':
    solution = Solution()

    # Input: stones = [2, 7, 4, 1, 8, 1]
    # Output: 1
    print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))

    # Input: stones = [1]
    # Output: 1
    print(solution.lastStoneWeight([1]))
