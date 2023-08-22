class Solution:
    def maxLength(self, arr: List[str]) -> int:
            
        def is_unique(s):
            return len(s) == len(set(s))
        
        def backtrack(start, current):
            nonlocal max_length
            
            if start == len(arr):
                if is_unique(current):
                    max_length = max(max_length, len(current))
                return
            
            backtrack(start + 1, current + arr[start])
            
            backtrack(start + 1, current)
        
        max_length = 0
        backtrack(0, "")
        return max_length