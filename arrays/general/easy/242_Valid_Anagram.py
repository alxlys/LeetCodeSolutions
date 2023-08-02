# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        for c in s:
            if c in char_map:
                char_map[c] = char_map[c] + 1
            else:
                char_map[c] = 1

        for c in t:
            char_count = char_map[c] if c in char_map else None
            if char_count is None:
                return False
            char_count -= 1
            if not char_count:
                del char_map[c]
            else:
                char_map[c] = char_count

        return len(char_map) == 0


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "anagram", t = "nagaram"
    # Output: true
    print(solution.isAnagram('anagram', 'nagaram'))

    # Input: s = "rat", t = "car"
    # Output: false
    print(solution.isAnagram('rat', 'car'))
