# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
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
    # my clumsy solution
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        slow_stack = [slow.val]
        while fast and fast.next:
            slow = slow.next
            slow_stack.append(slow.val)
            fast = fast.next.next

        max_twin_sum = 0
        slow = slow.next
        while slow:
            max_twin_sum = max(max_twin_sum, slow.val + slow_stack.pop())
            slow = slow.next

        return max_twin_sum

    # elegant neetcode solution
    def pair_sum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: head = [5, 4, 2, 1]
    # Output: 6
    print(solution.pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1))))))

    # Input: head = [4, 2, 2, 3]
    # Output: 7
    print(solution.pairSum(ListNode(4, ListNode(2, ListNode(2, ListNode(3))))))

    # Input: head = [1, 100000]
    # Output: 100001
    print(solution.pairSum(ListNode(1, ListNode(100000))))
