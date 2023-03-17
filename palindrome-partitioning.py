class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        L,R = 0,len(s) -1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True
    def backtrack(self,s,i,ans,res):
        if i == len(s):
            ans.append(res.copy())
            return
        for j in range(i+1,len(s)+1):
            if self.isPalindrome(s[i:j]):
                res.append(s[i:j])
                self.backtrack(s,j,ans,res)
                res.pop()
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.backtrack(s,0,ans,[])
        return(ans)