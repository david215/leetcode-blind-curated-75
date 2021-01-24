class Solution:

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in d:
                j = d[complement]
                return [i, j]
            else:
                d[n] = i


if __name__ == "__main__":
    s = Solution()

