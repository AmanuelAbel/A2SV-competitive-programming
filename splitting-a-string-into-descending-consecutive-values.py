class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        def backtrack(s):
            if not s:
                if len(ans) > 1:
                    return True 
                return False
            
            for i in range(1, len(s) +1 ):
                if len(ans) == 0 or int(ans[-1]) == int(s[:i]) + 1:
                    ans.append(int(s[:i]))
                    if backtrack(s[i:]):
                        return True
            if ans:
                ans.pop()
            return 
        return backtrack(s)