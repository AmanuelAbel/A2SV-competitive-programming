class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cache = defaultdict(int)
        for i in range(len(arr)-1,-1,-1):
            cache[arr[i]] = 1 + cache[arr[i]+difference]
        return max(cache.values())