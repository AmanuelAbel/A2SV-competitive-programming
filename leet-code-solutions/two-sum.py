class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        refer = {}
        
        for i ,n in enumerate(nums):
            val = target - n
            if val in refer:
                return[refer[val],i]
            refer[n] = i 