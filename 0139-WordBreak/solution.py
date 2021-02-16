class Solution:

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def dfs(i: int) -> bool:
        if i == len(s):
            return True
        elif i in memo:
            return memo[i]
        else:
            substr = s[i:]
            memo[i] = any(substr.startswith(word) and dfs(i + len(word)) for word in wordDict)
            return memo[i]

    # memo[i] is true if s[i:] can be formed with words in wordDict
    # memo[i] is false if s[i:] cannot be formed with words in wordDcit
    # if i not in memo, we do not yet know if s[i:] can be formed with words in wordDict
    memo = {}
    return dfs(0)


if __name__ == "__main__":
    s = Solution()

