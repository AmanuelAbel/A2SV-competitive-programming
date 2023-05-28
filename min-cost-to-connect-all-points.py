class UnionFind:
	def __init__(self,size):
		self.size = size
		self.root = [i for i in range(self.size)]
		self.rank = [0]*self.size

	def findRoot(self,x):
		if self.root[x] == x:
			return x
		self.root[x] = self.findRoot(self.root[x])                
		return self.root[x]

	def isConnected(self, x, y):
		rootX = self.findRoot(x)
		rootY = self.findRoot(y)
		return rootX == rootY

	def union(self,x,y):
		rootX = self.findRoot(x)
		rootY = self.findRoot(y)
		if rootX != rootY:                
			if self.rank[rootX]>self.rank[rootY]:
				self.root[rootY] = rootX
			elif self.rank[rootX]<self.rank[rootY]:
				self.root[rootX] = rootY
			else:
				self.root[rootY] = rootX
				self.rank[rootX] +=1    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(i,j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) 

        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                heapq.heappush(edges, (distance(i,j), i, j))

        graph = UnionFind(len(points))
        ret = 0
        count = 1
        while count<len(points):
            dist, i, j = heapq.heappop(edges)
            
            if graph.isConnected(i,j):
                continue

            graph.union(i,j)
            ret += dist
            count+=1

        return ret