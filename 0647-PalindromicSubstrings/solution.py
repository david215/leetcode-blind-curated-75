class Solution:

    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s) - 1
        for i in range(n):
            res += self.helper(s, i, i)
            res += self.helper(s, i, i + 1)
        res += self.helper(s, n, n)
        return res

    def helper(self, s: str, i:int, j:int) -> int:
        res = 0
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            else:
                break
        return res

if __name__ == "__main__":
    s = Solution()

