class Solution:

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    res = 0
    intervals.sort(key=lambda interval: interval[0])  # sort by start time
    hq = []  # min heapq of end time
    for interval in intervals:
        start, end = interval
        while hq and hq[0] <= start:
            heapq.heappop(hq)
        heapq.heappush(hq, end)
        res = max(res, len(hq))
    return res


if __name__ == "__main__":
    s = Solution()

