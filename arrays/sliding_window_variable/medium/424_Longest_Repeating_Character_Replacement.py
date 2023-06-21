# https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
        # count_map = {}
        # left, max_sub_str_len = 0, 0
        #
        # for right in range(len(s)):
        #     count_map[s[right]] = count_map.get(s[right], 0) + 1
        #
        #     while (right - left + 1) - max(count_map.values()) > k:
        #         count_map[s[left]] -= count_map.get(s[left]) - 1
        #         left += 1
        #
        #     max_sub_str_len = max(max_sub_str_len, right - left + 1)
        # return max_sub_str_len


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "ABAB", k = 2
    # Output: 4
    # print(solution.characterReplacement('ABAB', 2))

    # Input: s = "AABABBA", k = 1
    # Output: 4
    # print(solution.characterReplacement('AABABBA', 1))

    print(solution.characterReplacement('ABAA', 0))
