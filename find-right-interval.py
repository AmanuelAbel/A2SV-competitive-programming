class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort()
        ans = [-1] * len(intervals)
        start = []
        for i in intervals:
            start.append(i[0])
        for i in intervals:
            res = bisect_left(start, i[1])
            if res < len(intervals):
                ans[i[2]]= intervals[res][2]
        return ans