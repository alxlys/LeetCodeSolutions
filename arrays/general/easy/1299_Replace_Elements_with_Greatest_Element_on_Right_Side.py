# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(curr_max, arr[i])
            arr[i] = curr_max
            curr_max = new_max
        return arr


if __name__ == '__main__':
    solution = Solution()

    # Input: arr = [17, 18, 5, 4, 6, 1]
    # Output: [18, 6, 6, 6, 1, -1]
    print(solution.replaceElements([17, 18, 5, 4, 6, 1]))

    # Input: arr = [400]
    # Output: [-1]
    print(solution.replaceElements([400]))
