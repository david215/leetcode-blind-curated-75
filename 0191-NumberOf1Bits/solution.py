class Solution:

    d = {0: 0, 1: 1}

    def hamming_weight(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        else:
            res = 1 if n & 0b1 else 0
            res += self.hamming_weight(n >> 1)
            self.d[n] = res
            return res


if __name__ == "__main__":
    s = Solution()
    print(s.hamming_weight(0b11111111111111111111111111111101))

