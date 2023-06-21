# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_cache = set()
        max_sub_str_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in char_cache:
                char_cache.remove(s[left])
                left += 1
            max_sub_str_len = max(max_sub_str_len, right - left + 1)
            char_cache.add(s[right])
        return max_sub_str_len


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "abcabcbb"
    # Output: 3
    print(solution.lengthOfLongestSubstring('abcabcbb'))

    # Input: s = "bbbbb"
    # Output: 1
    print(solution.lengthOfLongestSubstring('bbbbb'))

    # Input: s = "pwwkew"
    # Output: 3
    print(solution.lengthOfLongestSubstring('pwwkew'))
