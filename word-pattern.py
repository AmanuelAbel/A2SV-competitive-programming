class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(map(list,s.split(" ")))
        s2 = []
        for i in s:
           x = "".join(i)
           s2.append(x)
        count = defaultdict(list)
        type1 = Counter(pattern)
        type2 = Counter(s2)
        s = s2
        if len(type1) != len(type2) or len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if not count[pattern[i]]:
                count[pattern[i]] = s[i]
            else:
                if count[pattern[i]] != s[i] :
                    return False
        return True