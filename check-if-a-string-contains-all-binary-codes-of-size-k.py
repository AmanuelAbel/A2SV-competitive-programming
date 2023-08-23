class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num = (2**k) 
        set1 = set()
        for i in range(len(s)-k+1):
            set1.add((s[i:i+k]))
        return len(set1) >= num