# https://leetcode.com/problems/boats-to-save-people/
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0

        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            count += 1
        return count


if __name__ == '__main__':
    solution = Solution()

    # Input: people = [1, 2], limit = 3
    # Output: 1
    print(solution.numRescueBoats([1, 2], 3))

    # Input: people = [3, 2, 2, 1], limit = 3
    # Output: 3
    print(solution.numRescueBoats([3, 2, 2, 1], 3))

    # Input: people = [3, 5, 3, 4], limit = 5
    # Output: 4
    print(solution.numRescueBoats([3, 5, 3, 4], 5))

    # Input: [2,2], limit = 6
    # Output: 1
    print(solution.numRescueBoats([2, 2], 6))
