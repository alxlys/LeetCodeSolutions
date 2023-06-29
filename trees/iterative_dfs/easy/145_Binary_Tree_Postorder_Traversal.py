# https://leetcode.com/problems/binary-tree-postorder-traversal/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visit = [False]
        while stack:
            curr, visited = stack.pop(), visit.pop()
            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: root = [1, null, 2, 3]
    # Output: [3, 2, 1]
    print(solution.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))

    # Input: root = []
    # Output: []
    print(solution.postorderTraversal(None))

    # Input: root = [1]
    # Output: [1]
    print(solution.postorderTraversal(TreeNode(1)))
