# https://leetcode.com/problems/reverse-linked-list/
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == '__main__':
    solution = Solution()

    # Input: head = [1, 2, 3, 4, 5]
    # Output: [5, 4, 3, 2, 1]

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    reversed_list = solution.reverseList(head)
    print(reversed_list)
