# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                res.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [1, null, 2, 3]
    # Output: [1, 2, 3]
    print(solution.preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))

    # Input: root = []
    # Output: []
    print(solution.preorderTraversal(None))

    # Input: root = [1]
    # Output: [1]
    print(solution.preorderTraversal(TreeNode(1)))
