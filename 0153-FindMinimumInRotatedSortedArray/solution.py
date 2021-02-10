class Solution:

    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while nums[i] > nums[j]:
            m = (j - i) // 2
            if nums[i] > nums[m]:
                j = m
            elif nums[m + 1] > nums[j]:
                i = m + 1
            else:
                i = m + 1
                break
        return nums[i]


if __name__ == "__main__":
    s = Solution()

