# https://leetcode.com/problems/my-calendar-i/
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True

        return self._insert(self.root, start, end)

    def _insert(self, node, start, end):
        if end <= node.start:
            if node.left:
                return self._insert(node.left, start, end)
            else:
                node.left = Node(start, end)
                return True
        elif start >= node.end:
            if node.right:
                return self._insert(node.right, start, end)
            else:
                node.right = Node(start, end)
                return True
        else:
            return False


if __name__ == '__main__':
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))  # return True
    print(myCalendar.book(15, 25))  # return False, It can not be booked because time 15
    # is already booked by another event.
    print(myCalendar.book(20, 30))  # return True, The event can be booked, as the first event takes every time
    # less than 20, but not including 20.
