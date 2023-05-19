class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        arr = []
        heapify(words)
        for i in count:
            arr.append((-count[i],i))
        arr.sort()
        res = []
        for i in range(min(len(arr),k)):
            res.append(arr[i][1])
        return res