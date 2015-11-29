import copy
class Solution(object):
    def dfs (self, a, idx, summ, target, solution, solutions):
        if summ > target:
            return
        if summ == target:
            solutions.append(copy.deepcopy(solution))
            return
        for i in range(len(a)):
            if i >= idx:
                self.dfs(a, i, summ+a[i], target, solution+[a[i]], solutions)
    
    def combinationSum(self, candidates, target):
        candidates.sort()
        solutions = []
        self.dfs(candidates, -1, 0, target,[], solutions)
        return solutions
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
