class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        count = 0
        for i in range(len(satisfaction)):
            count += (satisfaction[i]*(i+1))
        for i in range(len(satisfaction)):
            num = count
            if (count -  satisfaction[i] - sum(satisfaction[i+1:])) < count:
                return count
            else:
                count = num -  satisfaction[i] - sum(satisfaction[i+1:])
        return count