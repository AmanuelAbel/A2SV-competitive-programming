from collections import Counter, defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter1 = Counter(p)
        counter = defaultdict(int)
        l=0
        r=0
        res = []
        while r < len(s):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            
            if r - l + 1== len(p):
                if counter1 == counter:
                    res.append(l)
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            r += 1
        return res