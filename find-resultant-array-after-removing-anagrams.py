class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = defaultdict(list)
        ans = []
        def isAnagram(s,st):
            count1 = Counter(s)
            count2 = Counter(st)
            return count1 == count2
        if len(words) > 0:
            ans.append(words[0])
        for i in range(1,len(words)):
            if isAnagram(words[i],words[i-1]):
                print(words[i])
                continue
            ans.append(words[i])
        return ans