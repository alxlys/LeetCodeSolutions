# https://leetcode.com/problems/course-schedule-ii/
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        top_sort = []
        path = set()
        visited = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)
            for prerequisite in adj[node]:
                if not dfs(prerequisite):
                    return False
            path.remove(node)
            visited.add(node)
            top_sort.append(node)
            return True

        for c in range(numCourses):
            res = dfs(c)
            if not res:
                return []

        return top_sort


if __name__ == '__main__':
    solution = Solution()

    # Input: numCourses = 2, prerequisites = [[1, 0]]
    # Output: [0, 1]
    print(solution.findOrder(2, [[1, 0]]))

    # Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    # Output: [0, 2, 1, 3]
    print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

    # Input: numCourses = 1, prerequisites = []
    # Output: [0]
    print(solution.findOrder(1, []))

    print(solution.findOrder(2, [[0, 1], [1, 0]]))
