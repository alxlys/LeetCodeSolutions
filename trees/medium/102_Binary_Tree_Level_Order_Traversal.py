# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [3, 9, 20, null, null, 15, 7]
    # Output: [[3], [9, 20], [15, 7]]
    print(solution.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

    # Input: root = [1]
    # Output: [[1]]
    print(solution.levelOrder(TreeNode(1)))

    # Input: root = []
    # Output: []
    print(solution.levelOrder(None))
