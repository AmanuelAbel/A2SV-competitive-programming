class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        count = {}
        res = 0
        for r in range(len(s)):
            while  s[r] in count:
                count.pop(s[l])
                l+=1
            count[s[r]] = 1
            res = max(res,r-l+1)
        return res