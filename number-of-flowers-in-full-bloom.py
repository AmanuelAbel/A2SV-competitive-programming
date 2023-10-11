class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        arr = []
        for i in people:
            arr.append(bisect_right(start, i) - bisect_left(end, i))
        return arr