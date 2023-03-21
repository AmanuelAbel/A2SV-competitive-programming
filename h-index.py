class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        left = 0
        n = len(citations)
        right = len(citations) - 1
        while left <= right:
            mid = (right+left) // 2
            if len(citations) - mid > citations[mid]:
                left = mid + 1
            elif len(citations)- mid < citations[mid]:
                right = mid - 1
            else:
                return citations[mid]
        return len(citations) - left