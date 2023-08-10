# https://leetcode.com/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    curr_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if curr_sum > target:
                        d -= 1
                    elif curr_sum < target:
                        c += 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
        return res

    def fourSum_neetcode(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[r] * N:
                return
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i - 1] != nums[i]):
                        findNsum(i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums) - 1, target, 4, [], results)
        return results


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 0, -1, 0, -2, 2], target = 0
    # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))

    # Input: nums = [2, 2, 2, 2, 2], target = 8
    # Output: [[2, 2, 2, 2]]
    print(solution.fourSum([2, 2, 2, 2, 2], 8))
