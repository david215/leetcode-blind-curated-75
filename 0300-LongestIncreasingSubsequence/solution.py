class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(x: int) -> int:
            i, j = 0, len(dp) - 1
            while i <= j:
                m = (i + j) // 2
                if x < dp[m]:
                    j = m - 1
                elif x > dp[m]:
                    i = m + 1
                else:
                    return m
            return i

        dp = []
        for num in nums:
            i = binary_search(num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)


if __name__ == "__main__":
    s = Solution()

