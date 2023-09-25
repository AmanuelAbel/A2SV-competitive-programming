class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pair = [[scores[i] ,ages[i]] for i in range(len(ages))]
        pair.sort()
        dp = [pair[i][0] for i in range(len(pair))]

        for i in range(len(pair)):
            newscore, newage = pair[i]
            for j in range(i):
                score , age = pair[j]
                if newage >= age:
                    dp[i] = max(dp[i],newscore + dp[j])
        return max(dp)