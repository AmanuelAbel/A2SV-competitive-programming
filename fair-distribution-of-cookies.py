class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        array = [0]*k
        res = float("inf")
        cookies.sort(reverse=True)
        def backtrack(i):
            nonlocal res
            if i == len(cookies):
                res = min(res, max(array))
                return
            if res < max(array):
                return
            for j in range(k):
                array[j] += cookies[i]
                backtrack(i+1)
                array[j] -= cookies[i] 

        backtrack(0)
        return res