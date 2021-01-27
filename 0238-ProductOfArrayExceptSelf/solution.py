class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1 for _ in range(l)]
        pre_prev, post_prev = 1, 1
        for i in range(1, l):
            pre_prev *= nums[i - 1]
            post_prev *= nums[l - i]
            res[i] *= pre_prev
            res[l - i - 1] *= post_prev
        return res


if __name__ == "__main__":
    s = Solution()

