# https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for source, target in prerequisites:
            if source in graph:
                graph.get(source).append(target)
            else:
                graph[source] = []
                graph[source].append(target)

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            deps = graph.get(node)
            if not deps:
                return True

            visited.add(node)
            for dep in deps:
                if not dfs(dep):
                    return False
            visited.remove(node)
            graph[node].clear()
            return True

        for _node in range(numCourses):
            if not dfs(_node):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()

    # Input: numCourses = 2, prerequisites = [[1, 0]]
    # Output: true
    print(solution.canFinish(2, [[1, 0]]))

    # Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
    # Output: false
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
