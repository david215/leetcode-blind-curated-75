class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if not intervals:
            return res
        intervals.sort(key=lambda interval: interval[0])  # sort by start time
        prev = intervals[0]
        for curr in islice(intervals, 1, None):
            if prev[1] > curr[0]:
                res += 1
                if prev[1] > curr[1]:
                    prev = curr
            else:
                prev = curr
        return res


if __name__ == "__main__":
    s = Solution()

