class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [0]*26
        arr = []
        for i in range(26):
            parent[i] = i
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        def union(a,b):
            x = find(a)
            y = find(b)
            if x == y:
                return 
            parent[y] = x
            return 
        for i in range(len(equations)):
            if equations[i][1] == "=":
                union(ord(equations[i][0])- 97,ord(equations[i][3])-97)
            else:
                arr.append(equations[i])
        for i in range(len(arr)):
            if find(ord(arr[i][0])-97) == find(ord(arr[i][3])-97):
                return False
        return True