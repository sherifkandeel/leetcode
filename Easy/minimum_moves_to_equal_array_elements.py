class Solution(object):
    def minMoves(self, nums):
        biggest = max(nums)
        diffs =  [biggest - i for i in nums]
        biggestInverted = max(diffs)
        diffsInverted = [biggestInverted - i for i in diffs]
        return sum(diffsInverted)

