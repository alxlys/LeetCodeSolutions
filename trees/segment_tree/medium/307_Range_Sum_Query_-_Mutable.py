# https://leetcode.com/problems/range-sum-query-mutable/
from typing import List


class NumArray:
    class SegmentTree:
        def __init__(self, total, L, R):
            self.total_sum = total
            self.left, self.right = None, None
            self.L = L
            self.R = R

        @staticmethod
        def build(nums, L, R):
            if L == R:
                return NumArray.SegmentTree(nums[L], L, R)
            M = (L + R) // 2
            root = NumArray.SegmentTree(0, L, R)
            root.left = NumArray.SegmentTree.build(nums, L, M)
            root.right = NumArray.SegmentTree.build(nums, M + 1, R)
            root.total_sum = root.left.total_sum + root.right.total_sum
            return root

        def update(self, index, val):
            if self.L == self.R:
                self.total_sum = val
                return
            M = (self.L + self.R) // 2
            if index > M:
                self.right.update(index, val)
            else:
                self.left.update(index, val)
            self.total_sum = self.left.total_sum + self.right.total_sum

        def range_query(self, L, R):
            if self.L == L and self.R == R:
                return self.total_sum
            M = (self.L + self.R) // 2
            if L > M:
                return self.right.range_query(L, R)
            elif R <= M:
                return self.left.range_query(L, R)
            else:
                return self.left.range_query(L, M) + self.right.range_query(M + 1, R)

    def __init__(self, nums: List[int]):
        self.tree = NumArray.SegmentTree.build(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.range_query(left, right)


if __name__ == '__main__':
    numArray = NumArray([1, 3, 5])
    print(numArray.sumRange(0, 2))  # return 1 + 3 + 5 = 9
    numArray.update(1, 2)  # nums = [1, 2, 5]
    print(numArray.sumRange(0, 2))  # return 1 + 2 + 5 = 8
