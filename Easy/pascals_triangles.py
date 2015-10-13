class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            lvl = []
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1,1])
            else:
                for j in range(i):
                    if j == 0:
                        lvl.append(1)
                    else:
                        lvl.append(triangle[len(triangle) - 1][j-1] + triangle[len(triangle) - 1][j])
                lvl.append(1)
                triangle.append(lvl)
        return triangle
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
