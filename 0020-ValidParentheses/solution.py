class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif stack:
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:  # c == ']'
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        return not stack


if __name__ == "__main__":
    s = Solution()

