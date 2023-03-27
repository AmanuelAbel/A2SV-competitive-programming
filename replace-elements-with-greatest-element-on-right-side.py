class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        var = -1
        ans = []
        for i in range(len(arr)-1,-1,-1):
            ans.append(var)
            var = max(var,arr[i])
        ans.reverse()
        return ans