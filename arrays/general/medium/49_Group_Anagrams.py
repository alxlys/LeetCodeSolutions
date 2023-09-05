# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            key = tuple(sorted(s))
            value = anagram_map.get(key, [])
            value.append(s)
            anagram_map[key] = value
        return list(anagram_map.values())


if __name__ == '__main__':
    solution = Solution()

    # Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    # Input: strs = [""]
    # Output: [[""]]
    print(solution.groupAnagrams(['']))

    # Input: strs = ["a"]
    # Output: [["a"]]
    print(solution.groupAnagrams(["a"]))
