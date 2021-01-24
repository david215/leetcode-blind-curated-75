class Solution:

    def can_attend_meetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda interval : interval[0]) # sort by start time
        return all(x[1] <= y[0] for x, y in zip(interval[:-1], interval[1:]))


if __name__ == "__main__":
    s = Solution()

