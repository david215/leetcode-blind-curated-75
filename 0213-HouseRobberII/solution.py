class Solution:

    def rob(self, nums: List[int]) -> int:
        res0, res1, prev0, prev1 = 0, 0, 0, 0

        res0 = nums[0]  # first house
        for n in islice(nums, 1, len(nums) - 1):  # houses in between
            res0, prev0 = max(res0, prev0 + n), res0
            res1, prev1 = max(res1, prev1 + n), res1
        res1 = max(res1, prev1 + nums[-1])  # last house

        return max(res0, res1)


if __name__ == "__main__":
    s = Solution()

