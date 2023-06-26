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
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [3, 1, 4, null, 2], k = 1
    # Output: 1
    print(solution.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1))
