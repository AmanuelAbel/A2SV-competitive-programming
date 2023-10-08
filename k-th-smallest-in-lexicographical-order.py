class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(prefix, n):
            count = 0
            cur = prefix
            next_cur = prefix + 1
            while cur <= n:
                count += min(n + 1, next_cur) - cur
                cur *= 10
                next_cur *= 10
            return count
        
        prefix = 1
        p = 1
        
        while p < k:
            count_from_prefix = count(prefix, n)
            
            if p + count_from_prefix <= k:
                prefix += 1
                p += count_from_prefix
            else:
                prefix *= 10
                p += 1
        
        return prefix