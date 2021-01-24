class Solution:

    def countBits(self, num: int) -> List[int]:
        res = [0]
        if num == 0:
            return res
        res.append(1)
        curr = 1
        for i in range(2, num + 1):
            if i == curr * 2:
                res.append(1)
                curr = i
            else:
                res.append(res[curr] + res[i - curr])
        return res


if __name__ == "__main__":
    s = Solution()

