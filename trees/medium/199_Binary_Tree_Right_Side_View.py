# https://leetcode.com/problems/binary-tree-right-side-view/
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            val = None
            for i in range(len(queue)):
                node = queue.popleft()
                val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if val is not None:
                res.append(val)
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [1, 2, 3, null, 5, null, 4]
    # Output: [1, 3, 4]
    print(solution.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))

    # Input: root = [1, null, 3]
    # Output: [1, 3]
    print(solution.rightSideView(TreeNode(1, None, TreeNode(3))))

    # Input: root = []
    # Output: []
    print(solution.rightSideView(None))

    print(solution.rightSideView(
        TreeNode(1, TreeNode(2, None, TreeNode(5, TreeNode(7))), TreeNode(3, None, TreeNode(4)))))
