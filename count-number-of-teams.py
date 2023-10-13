class Solution:
    def numTeams(self, rating: List[int]) -> int:
        high = [0]*len(rating)
        low = [0] * len(rating)
        count = 0
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[i] < rating[j]:
                    high[i] += 1
                elif rating[i] > rating[j]:
                    low[i] += 1
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[i] < rating[j]:
                    count += high[j]
                if rating[i] > rating[j]:
                    count += low[j]

        return count