class Solution:
    def isprime(num):
            for n in range(2,int(num**0.5)+1):
                if num%n==0:
                    return False
            return True
    nums = defaultdict(int)
    nums[1] = 0
    nums[2] = 2
    for i in range(3,1001):
        if isprime(i):
            nums[i] = i
        else:
            for z in range (2,i):
                if i // z in nums and (i//z) * z == i:
                    nums[i] = nums[i//z] + nums[z]
                    break
    def minSteps(self, n: int) -> int:
        return self.nums[n]