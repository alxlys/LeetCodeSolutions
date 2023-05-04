# https://leetcode.com/problems/design-linked-list/
class Node:
    def __init__(self, val, _next, prev):
        self.val = val
        self.next = _next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        dummy_tail = Node(666, None, None)
        dummy_head = Node(999, dummy_tail, None)
        dummy_tail.prev = dummy_head
        self.head = dummy_head
        self.tail = dummy_tail
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.length - 1:
            return -1
        current = self.head.next
        idx = 0
        while idx != index:
            current = current.next
            idx += 1
        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head.next, self.head)
        self.head.next.prev = node
        self.head.next = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            # invalid index
            return
        elif index == self.length:
            self.addAtTail(val)
        else:
            current = self.head.next
            idx = 0
            while idx != index:
                current = current.next
                idx += 1
            node = Node(val, current, current.prev)
            current.prev.next = node
            current.prev = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1:
            # invalid index
            return
        else:
            current = self.head.next
            idx = 0
            while idx != index:
                current = current.next
                idx += 1
            current.prev.next = current.next
            current.next.prev = current.prev
            self.length -= 1


if __name__ == '__main__':
    # myLinkedList = MyLinkedList()
    # myLinkedList.addAtHead(1)
    # myLinkedList.addAtTail(3)
    # myLinkedList.addAtIndex(1, 2)  # linkedlist becomes 1->2->3
    # print(myLinkedList.get(1))  # return 2
    # myLinkedList.deleteAtIndex(1)  # now the linked list is 1->3
    # print(myLinkedList.get(1))  # return 3

    # ["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtHead", "deleteAtIndex", "addAtHead", "get", "get", "get",
    #  "addAtHead", "deleteAtIndex"]
    # [[], [4], [1], [1], [5], [3], [7], [3], [3], [3], [1], [4]]
    # myLinkedList = MyLinkedList()
    # myLinkedList.addAtHead(4)
    # print(myLinkedList.get(1))
    # myLinkedList.addAtHead(1)
    # myLinkedList.addAtHead(5)
    # myLinkedList.deleteAtIndex(3)
    # myLinkedList.addAtHead(7)
    # print(myLinkedList.get(3))
    # print(myLinkedList.get(3))
    # print(myLinkedList.get(3))
    # myLinkedList.addAtHead(1)
    # myLinkedList.deleteAtIndex(4)

    # ["MyLinkedList", "addAtHead", "addAtTail", "deleteAtIndex", "addAtTail", "addAtIndex", "addAtIndex",
    #  "deleteAtIndex", "deleteAtIndex", "addAtTail", "addAtIndex", "addAtTail"]
    # [[], [7], [0], [1], [5], [1, 1], [2, 6], [2], [1], [7], [1, 7], [6]]
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(7)
    myLinkedList.addAtTail(0)
    myLinkedList.deleteAtIndex(1)
    myLinkedList.addAtTail(5)
    myLinkedList.addAtIndex(1, 1)
    myLinkedList.addAtIndex(2, 6)
    myLinkedList.deleteAtIndex(2)
    myLinkedList.deleteAtIndex(1)
    myLinkedList.addAtTail(7)
    myLinkedList.addAtIndex(1, 7)
    myLinkedList.addAtTail(6)



