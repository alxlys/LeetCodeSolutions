# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.__inorder__(root, arr, k)
        return arr[len(arr) - 1]

    def __inorder__(self, node: TreeNode, arr: List[int], k: int) -> None:
        if not node:
            return
        self.__inorder__(node.left, arr, k)
        if len(arr) < k:
            arr.append(node.val)
        if len(arr) == k:
            return
        self.__inorder__(node.right, arr, k)


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [3, 1, 4, null, 2], k = 1
    # Output: 1
    print(solution.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1))
