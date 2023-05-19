# https://leetcode.com/problems/path-sum/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
            return True
        elif self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum):
            return True
        targetSum += root.val
        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
    # Output: true
    print(solution.hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                                       TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22))

    # Input: root = [1, 2, 3], targetSum = 5
    # Output: false
    print(solution.hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))

    # Input: root = [], targetSum = 0
    # Output: false
    print(solution.hasPathSum(None, 0))
