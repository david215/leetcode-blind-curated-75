class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for c in filter(lambda c: c <= amount, coins):
            dp[c] = 1
        for i in range(amount + 1):
            if dp[i] != float('inf'):
                continue
            rest_min_count = float('inf')
            for c in filter(lambda c: i - c > 0, coins):
                rest_min_count = min(rest_min_count, dp[i - c])
            dp[i] = 1 + rest_min_count if rest_min_count != float('inf') else float('inf')

        res = dp[amount]
        return res if res != float('inf') else -1


if __name__ == "__main__":
    s = Solution()

