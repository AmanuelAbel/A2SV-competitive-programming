class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        l,r = points[0][0],points[0][1]
        count = 1
        for i in range(len(points)):
            if r < points[i][0] or l > points[i][0]:
                count += 1
                l = points[i][0]
                r = points[i][1]
            else:
                l = min(l,points[0][0])
                r = min (r,points[i][1])
        return count