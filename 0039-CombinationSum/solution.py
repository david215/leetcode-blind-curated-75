class Solution:

    def combination_sum(self, nums: list[int], target: int) -> list[list[int]]:
        def backtrack(curr: list[int], rem: int, i: int) -> None:
            if rem == 0:
                res.append(curr[:])
            elif rem > 0:
                for j in range(i, len(nums)):
                    n = nums[j]
                    if (rem - n) < 0:
                        break
                    curr.append(n)
                    backtrack(curr, rem - n, j)
                    curr.pop()
        nums.sort()
        res = []
        backtrack([], target, 0)
        return res


if __name__ == "__main__":
    s = Solution()

