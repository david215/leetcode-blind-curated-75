class Solution:

    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31):
            b = n & 1
            res |= b
            n >>= 1
            res <<= 1
        res |= n
        return res


if __name__ == "__main__":
    s = Solution()

