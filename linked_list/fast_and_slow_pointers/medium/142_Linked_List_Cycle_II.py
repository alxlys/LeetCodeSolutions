# https://leetcode.com/problems/linked-list-cycle-ii/
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                cycle = True
                break
        if not cycle:
            return None
        slow_2 = head
        while slow != slow_2:
            slow = slow.next
            slow_2 = slow_2.next
        return slow


if __name__ == '__main__':
    solution = Solution()

    # Input: head = [3, 2, 0, -4], pos = 1
    # Output: tail connects to node index 1
    node0 = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    node0.next = node1
    node1.next = node2
    node2.next = node3

    node3.next = node1
    print(solution.detectCycle(node0).val)

    # Input: head = [1, 2], pos = 0
    # Output: tail connects to node index 0
    node0 = ListNode(1)
    node1 = ListNode(2)
    node0.next = node1
    node1.next = node0

    node1.next = node0
    print(solution.detectCycle(node0).val)

    # Input: head = [1], pos = -1
    # Output: no cycle
    res = solution.detectCycle(ListNode(1))
    print(res.val if res else None)
