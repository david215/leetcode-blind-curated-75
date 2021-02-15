class Solution:

    def rob(self, nums: List[int]) -> int:
        res, prev = 0, 0
        for n in nums:
            res, prev = max(res, prev + n), res
        return res


if __name__ == "__main__":
    s = Solution()

