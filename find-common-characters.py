class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = defaultdict(int)
        res = []
        for i in range(len(words[0])):
            count[words[0][i]] += 1
        for i in range(1,len(words)):
            word = Counter(words[i])
            arr = []
            for s in count:
                if s in word:
                    count[s] = min(count[s],word[s])
                else:
                    print(s)
                    arr.append(s)
            print(arr)
            for s in arr:
                count.pop(s)
        for i in count:
            for j in range(count[i]):
                res.append(i)
        return res