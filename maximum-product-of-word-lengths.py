class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n = len(words)
        bitmasks = [0] * n  
        max_product = 0
        for i in range(n):
            for char in words[i]:
                bitmasks[i] |= 1 << (ord(char) - ord('a'))
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product