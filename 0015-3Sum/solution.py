class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        end = len(nums) - 1
        i = 0
        while i <= end - 2:
            j = i + 1
            k = end
            a = nums[i]
            while j < k:
                b, c = nums[j], nums[k]
                sum_ = a + b + c
                if sum_ == 0:
                    res.append([a, b, c])
                    while nums[j] == b and j < k:
                        j += 1
                    while nums[k] == c and j < k:
                        k -= 1
                elif sum_ < 0:
                    j += 1
                else:  # sum > 0
                    k -= 1
            while nums[i] == a and i <= end - 2:
                i += 1
        return res


if __name__ == "__main__":
    s = Solution()

