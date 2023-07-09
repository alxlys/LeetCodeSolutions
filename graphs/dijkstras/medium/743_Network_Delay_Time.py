# https://leetcode.com/problems/network-delay-time/
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for v in range(1, n + 1):
            graph[v] = []

        for source, dest, weight in times:
            graph[source].append((dest, weight))

        visited = set()
        min_heap = [[0, k]]
        time = 0

        while min_heap:
            curr_weight, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            time = max(time, curr_weight)

            for neighbour_node, neighbour_weight in graph[curr_node]:
                if neighbour_node not in visited:
                    heapq.heappush(min_heap, [curr_weight + neighbour_weight, neighbour_node])

        return time if len(visited) == n else -1


if __name__ == '__main__':
    solution = Solution()

    # Input: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
    # Output: 2
    print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

    # Input: times = [[1, 2, 1]], n = 2, k = 1
    # Output: 1
    print(solution.networkDelayTime([[1, 2, 1]], 2, 1))

    # Input: times = [[1, 2, 1]], n = 2, k = 2
    # Output: -1
    print(solution.networkDelayTime([[1, 2, 1]], 2, 2))
