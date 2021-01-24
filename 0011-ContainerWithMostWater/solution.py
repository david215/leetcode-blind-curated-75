class Solution:

    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            x = height[i]
            y = height[j]
            w = j - i
            h = min(x, y)
            res = max(res, w * h)
            if x < y:
                i += 1
            else:
                j -= 1
        return res


if __name__ == "__main__":
    s = Solution()

