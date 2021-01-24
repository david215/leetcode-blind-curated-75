class Solution:

    def max_profit(self, prices: list[int]):
        _min = float('inf')
        res = 0
        for p in prices:
            _min = min(_min, p)
            res = max(res, p - min)
        return res


if __name__ == "__main__":
    s = Solution()

