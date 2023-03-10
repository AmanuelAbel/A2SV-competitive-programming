class Solution:
    def helper(self,i,n,subs,k,comb):
        if len(subs) == k:
            comb.append(subs.copy())
            return 
        if i > n:
            return 
        subs.append(i)
        self.helper(i+1,n,subs,k,comb)
        subs.pop()
        self.helper(i+1,n,subs,k,comb)
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        subs = []
        self.helper(1,n,[],k,comb)
        return comb