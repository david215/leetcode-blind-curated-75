class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        res = prev = nums[0]
        for n in islice(nums, 1, None):  # start=1, continue until the end
            curr = max(prev, 0) + n
            res = max(res, curr)
            prev = curr
        return res


if __name__ == "__main__":
    s = Solution()

