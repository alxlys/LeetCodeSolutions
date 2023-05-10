# https://leetcode.com/problems/valid-parentheses/
class Solution:
    brackets = {')': '(', '}': '{', ']': '['}

    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for bracket in s:
            if bracket not in self.brackets.keys():
                stack.append(bracket)
            elif len(stack) == 0 or stack.pop() != self.brackets.get(bracket):
                return False
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()

    s = "()"
    print(solution.isValid(s))
    # Output: true

    s = "()[]{}"
    print(solution.isValid(s))
    # Output: true

    s = "(]"
    print(solution.isValid(s))
    # Output: false
