# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwich_idx = 0
        students_rotated = 0
        while sandwich_idx != len(sandwiches) and students_queue and students_rotated <= len(students_queue):
            student = students_queue.popleft()
            if student == sandwiches[sandwich_idx]:
                sandwich_idx += 1
                students_rotated = 0
            else:
                students_queue.append(student)
                students_rotated += 1
                students_queue.rotate(-1)
        return len(students_queue)


if __name__ == '__main__':
    solution = Solution()

    # Input: students = [1, 1, 0, 0], sandwiches = [0, 1, 0, 1]
    # Output: 0
    print(solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))

    # Input: students = [1, 1, 1, 0, 0, 1], sandwiches = [1, 0, 0, 0, 1, 1]
    # Output: 3
    print(solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
