class Solution:

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i], s[j]
            if not a.isalnum():
                i += 1
                continue
            if not b.isalnum():
                j -= 1
                continue
            if a.isalpha() and b.isalpha():
                a, b = a.lower(), b.lower()
            if a == b:
                i += 1
                j -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()

