# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        res = []

        i1, i2 = 0, 0
        while i1 < len1 and i2 < len2:
            res.append(word1[i1])
            res.append(word2[i2])
            i1 += 1
            i2 += 1

        if i1 < len1:
            res.append(word1[i1:])

        if i2 < len2:
            res.append(word2[i2:])

        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()

    # Input: word1 = "abc", word2 = "pqr"
    # Output: "apbqcr"
    print(solution.mergeAlternately("abc", "pqr"))

    # Input: word1 = "ab", word2 = "pqrs"
    # Output: "apbqrs"
    print(solution.mergeAlternately("ab", "pqrs"))
