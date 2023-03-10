class Solution:
    def helper(self,i,n,subs,k,comb):
        if len(subs) == k:
            comb.append(subs.copy())
            return 
        if i > n:
            return 
        for j in range(i,n+1):
            subs.append(j)
            self.helper(j+1,n,subs,k,comb)
            subs.pop()
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        subs = []
        self.helper(1,n,[],k,comb)
        return comb