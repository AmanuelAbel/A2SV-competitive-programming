class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = defaultdict(int)
        for i in range(len(edges)):
            for j in range(2):
                count[edges[i][j]] += 1
        for c in count:
            if count[c] == len(edges):
                return c