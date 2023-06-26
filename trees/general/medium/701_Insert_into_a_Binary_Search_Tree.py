# https://leetcode.com/problems/insert-into-a-binary-search-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [4, 2, 7, 1, 3], val = 5
    # Output: [4, 2, 7, 1, 3, 5]
    print(solution.insertIntoBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5))
