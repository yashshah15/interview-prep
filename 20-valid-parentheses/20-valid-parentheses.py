class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        
        for br in s:
            if brackets.get(br, False):
                stack.append(br)
            else:
                if len(stack) == 0:
                    return False

                last_bracket = stack.pop()
                if brackets[last_bracket] != br:
                    return False

        return len(stack) == 0