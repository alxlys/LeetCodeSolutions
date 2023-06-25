# https://leetcode.com/problems/linked-list-cycle/
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: head = [3, 2, 0, -4], pos = 1
    # Output: true
    node0 = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    node0.next = node1
    node1.next = node2
    node2.next = node3

    node3.next = node1
    print(solution.hasCycle(node0))

    # Input: head = [1, 2], pos = 0
    # Output: true
    node0 = ListNode(1)
    node1 = ListNode(2)
    node0.next = node1
    node1.next = node0

    node1.next = node0
    print(solution.hasCycle(node0))

    # Input: head = [1], pos = -1
    # Output: false
    print(solution.hasCycle(ListNode(1)))

    # [1, 2]
    print(solution.hasCycle(ListNode(1, ListNode(2))))
