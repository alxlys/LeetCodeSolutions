# https://leetcode.com/problems/clone-graph/
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        neighbors_vals = [str(neighbor.val) for neighbor in self.neighbors]
        return f"Node(val={self.val}, neighbors=[{', '.join(neighbors_vals)}])"


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        return self.__clone__(node, {})

    def __clone__(self, node, graph_map):
        if node.val in graph_map:
            return graph_map.get(node.val)
        cloned_node = Node(node.val)
        graph_map[node.val] = cloned_node
        for neighbor in node.neighbors:
            cloned_node.neighbors.append(self.__clone__(neighbor, graph_map))
        return cloned_node


if __name__ == '__main__':
    solution = Solution()

    # Input: adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    # Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    node_1.neighbors.append(node_2)
    node_1.neighbors.append(node_4)

    node_2.neighbors.append(node_1)
    node_2.neighbors.append(node_3)

    node_3.neighbors.append(node_2)
    node_3.neighbors.append(node_4)

    node_4.neighbors.append(node_1)
    node_4.neighbors.append(node_3)

    print(node_1)

    # Input: adjList = [[]]
    # Output: [[]]

    # Input: adjList = []
    # Output: []
