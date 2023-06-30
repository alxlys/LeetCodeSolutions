# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
        self.k = k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == '__main__':
    solution = KthLargest(3, [4, 5, 8, 2])
    print(solution.add(2))  # return 4
    print(solution.add(5))  # return 5
    print(solution.add(10))  # return 5
    print(solution.add(9))  # return 8
    print(solution.add(4))  # return 8
