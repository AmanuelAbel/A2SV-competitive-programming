class Solution(object):
    def dividePlayers(self, skill):
        target = sum(skill)//(len(skill)//2)
        cnt = Counter(skill)
        result = 0
        for k in cnt:
            if target-k not in cnt or cnt[target-k] != cnt[k]:
                return -1
            result += k*(target-k)*cnt[k]
        return result//2