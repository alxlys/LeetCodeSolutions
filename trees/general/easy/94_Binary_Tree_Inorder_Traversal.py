# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.__inorder__(root, arr)
        return arr

    def __inorder__(self, node: TreeNode, arr: List[int]) -> None:
        if not node:
            return
        self.__inorder__(node.left, arr)
        arr.append(node.val)
        self.__inorder__(node.right, arr)


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [1, null, 2, 3]
    # Output: [1, 3, 2]
    print(solution.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None))))

    # Input: root = []
    # Output: []
    print(solution.inorderTraversal(None))

    # Input: root = [1]
    # Output: [1]
    print(solution.inorderTraversal(TreeNode(1)))
