class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def winner(start,end,turn):
            if start == end:
                if turn:
                    return [nums[start],0]
                else:
                    return [0,nums[start]]
            choice1 = winner(start + 1,end,not turn )
            choice2 = winner(start,end - 1 ,not turn)
            if turn:
                if choice1[0] + nums[start] > choice2[0] + nums[end]:
                    choice1[0] += nums[start]
                    return choice1
                else:
                    choice2[0] += nums[end]
                    return choice2
            else:
                if choice2[1] + nums[end] > choice1[1] + nums[start]:
                    choice2[1] += nums[end]
                    return choice2
                else:
                    choice1[1] += nums[start]
                    return choice1
        player1, player2 = winner(0, len(nums) -1, True)
        print(player1)
        if player1 >= player2:
            return True
        else:
            return False
        return True