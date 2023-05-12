# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional


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
        if not lists:
            return None
        elif len(lists) < 2:
            return lists.pop()

        list_0 = lists.pop()
        while lists:
            list_1 = lists.pop()
            list_0 = self.__merge_two_lists__(list_0, list_1)

        return list_0

    def __merge_two_lists__(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

    # Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # Output: [1, 1, 2, 3, 4, 4, 5, 6]

    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))),
             ListNode(2, ListNode(6))]

    print(solution.mergeKLists(lists))
