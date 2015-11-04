#This can be done in constant space if we know that the matrix can only contain 0 or 1, by using first row and first column to mark 0 places
class Solution(object):
    def setZeroes(self, matrix):
        cols = set()
        for i in range(len(matrix)):
            delete_row = False
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.add(j)
                    delete_row = True
            if delete_row:
                matrix[i] = [0 for x in range(len(matrix[0]))]
                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in cols:
                    matrix[i][j] = 0
        
                
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
