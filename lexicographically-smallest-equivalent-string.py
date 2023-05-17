class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [0]*26
        for i in range(26):
            parent[i] = i
        def Find(n):
            if parent[n] != n:
                parent[n] = Find(parent[n])
            return parent[n]
        def Union(a, b):
            x = Find(a)
            y = Find(b)
            if x == y:
                return 
            if parent[x] > parent[y]:
                parent[x] = y
            else:
                parent[y] = x
            
            return 
        res = ""
        for i in range(len(s1)):
            Union(ord(s1[i]) - 97,ord(s2[i]) - 97)
        for i in baseStr:
            ans = Find(ord(i)-97)
            res += chr(ans+97)
        return res