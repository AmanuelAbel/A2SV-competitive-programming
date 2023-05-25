class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for i in bills:
            if i == 5:
                count[5] += 1
            if i == 10:
                if not count[5]:
                    return False
                else:
                    count[10] += 1
                    count[5] -= 1
            if i == 20:
                if not count[5]:
                    return False
                if not count[10] and count[5] < 3:
                    return False
                if count[10]:
                    count[10] -= 1
                    count[5] -= 1
                    continue
                if not count[10] and count[5]:
                    count[5] -= 3
            print(i,count)
            
        return True