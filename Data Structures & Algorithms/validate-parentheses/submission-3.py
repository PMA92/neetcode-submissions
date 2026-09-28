class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = [s[0]]
        left = ['(', '{', '[']
        right = [')', '}', ']']
        for i in range(1, len(s)):
            if s[i] in right:
                goal = left[right.index(s[i])]
                if len(stack) == 0 or stack[-1] != goal:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        else:
            return True

            