class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        visit = set()
        for c in count:
            if count[c] in visit:
                return False
            visit.add(count[c])
        return True