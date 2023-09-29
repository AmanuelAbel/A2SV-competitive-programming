class Solution:
    

    def insert(self,root, num):
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def find_max_xor(self,root, num):
        node = root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            if opposite_bit in node:
                xor |= (1 << i)
                node = node[opposite_bit]
            else:
                node = node[bit]
        return xor

    def findMaximumXOR(self, nums: List[int]) -> int:
            
        root = {}
        max_xor = 0
        

        for num in nums:
            self.insert(root, num)
        for num in nums:
            max_xor = max(max_xor, self.find_max_xor(root, num))


        return max_xor