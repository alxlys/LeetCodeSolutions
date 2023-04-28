# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        vals = []
        while node is not None:
            vals.append(str(node.val))
            node = node.next
        return "->".join(vals)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr

        while list1 or list2:
            if list1 and list2 and list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            elif list1 and list2:
                curr.next = list2
                list2 = list2.next
            elif list1:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        return head.next


if __name__ == '__main__':
    solution = Solution()

    # Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
    # Output: [1, 1, 2, 3, 4, 4]
    print(solution.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))

    # Input: list1 = [], list2 = []
    # Output: []
    print(solution.mergeTwoLists(None, None))

    # Input: list1 = [], list2 = [0]
    # Output: [0]
    print(solution.mergeTwoLists(None, ListNode(0)))
