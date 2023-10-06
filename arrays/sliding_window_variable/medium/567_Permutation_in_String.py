# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_char_map = {}
        for c in s1:
            s1_char_map[c] = 1 + s1_char_map.get(c, 0)

        l, r = 0, 0
        s2_char_map = {}
        s2_curr_len = 0
        s2_len = len(s2)
        while l <= r < s2_len:
            if s1_len == s2_curr_len or s1_len < s2_curr_len:
                s2_char_map[s2[l]] = s2_char_map.get(s2[l], 1) - 1
                if not s2_char_map[s2[l]]:
                    del s2_char_map[s2[l]]
                s2_curr_len -= 1
                l += 1
            elif s1_len > s2_curr_len:
                s2_char_map[s2[r]] = 1 + s2_char_map.get(s2[r], 0)
                r += 1
                s2_curr_len += 1

            if s1_len == s2_curr_len and s1_char_map == s2_char_map:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: s1 = "ab", s2 = "eidbaooo"
    # Output: true
    print(solution.checkInclusion("ab", "eidbaooo"))

    # Input: s1 = "ab", s2 = "eidboaoo"
    # Output: false
    print(solution.checkInclusion("ab", "eidboaoo"))

    print(solution.checkInclusion("adc", "dcda"))
