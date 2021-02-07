class Solution:

    def contains_duplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False


if __name__ == "__main__":
    s = Solution()

