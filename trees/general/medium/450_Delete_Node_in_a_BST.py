# https://leetcode.com/problems/delete-node-in-a-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.__find_min_node__(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root

    @staticmethod
    def __find_min_node__(root: TreeNode) -> TreeNode:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [5, 3, 6, 2, 4, null, 7], key = 3
    # Output: [5, 4, 6, 2, null, null, 7]
    print(solution.deleteNode(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 3))

    # Input: root = [5, 3, 6, 2, 4, null, 7], key = 0
    # Output: [5, 3, 6, 2, 4, null, 7]
    print(solution.deleteNode(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 0))
