# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional
import sys

max_int = sys.maxsize


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        values = []
        while node is not None:
            values.append(str(node.val))
            node = node.next
        return " -> ".join(values)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current = dummy_node
        while True:
            min_list_int = max_int
            min_list = None
            for l in lists:
                if l and l.val < min_list_int:
                    min_list_int = l.val
                    min_list = l
            if not min_list:
                break





if __name__ == '__main__':
    solution = Solution()

    # Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # Output: [1, 1, 2, 3, 4, 4, 5, 6]

    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))),
             ListNode(2, ListNode(6))]

    print(solution.mergeKLists(lists))
