class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]
        for curr in itertools.islice(intervals, 1, None):
            prev = res[-1]
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(curr)
        return res


if __name__ == "__main__":
    s = Solution()

