class Solution:

    def climb_stairs(self, n: int) -> int:
        if n < 3:
            return n
        prev = 1
        curr = 2
        for i in range(3, n + 1): # inclusive
            prev, curr = curr, prev + curr
        return curr

if __name__ == "__main__":
    s = Solution()

