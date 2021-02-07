from functools import reduce
from operator import add


class Solution:

    def missing_number(self, nums: list[int]) -> int:
        n = len(nums)
        _all = n * (n + 1) // 2
        return _all - sum(nums)


if __name__ == "__main__":
    s = Solution()

