class Solution:

    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            n = nums[m]
            if n == target:
                return m
            # at least one of left and right is sorted
            elif nums[i] <= n:  # left is sorted
                if nums[i] <= target and target < n:  # target in left
                    j = m - 1
                else:  # target in right
                    i = m + 1
            else:  # right is sorted
                if n < target and target <= nums[j]:  # target in right
                    i = m + 1
                else:  # target in left
                    j = m - 1
        return -1


if __name__ == "__main__":
    s = Solution()

