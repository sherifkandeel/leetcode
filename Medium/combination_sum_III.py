import copy
class Solution(object):
        def generate(self, ls, cur, num, n, k):
                    if num > 0:
                                    cur.append(num)
        if len(cur) == k:
                        if sum(cur) == n:
                                            ls.append(cur)
            return
        for i in range(num+1, 10):
                        self.generate(ls, copy.deepcopy(cur), i, n, k)

    def combinationSum3(self, k, n):
                ls = []
        self.generate(ls, [], 0, n, k)
        return ls
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
