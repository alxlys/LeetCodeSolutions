# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional


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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    solution = Solution()

    # Input: head = [1, 2, 3, 4, 5]
    # Output: [3, 4, 5]
    print(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

    # Input: head = [1, 2, 3, 4, 5, 6]
    # Output: [4, 5, 6]
    print(solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
