class Solution(object):
    def bs(slef, arr, target):
        start = 0
        end = len(arr[0])*len(arr)-1
        while start <= end:
            mid = start + (end-start)/2
            row = mid / len(arr[0])
            col = mid % len(arr[0])
            if target == arr[row][col]:
                return True
            if target> arr[row][col]:
                start = mid + 1
            elif target < arr[row][col]:
                end = mid - 1
        return False
                
            
    def searchMatrix(self, matrix, target):
        arr = []
        for i in matrix:
            arr.extend(i)
        if len(arr) == 1:
            return target in arr
        return self.bs(matrix, target)
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
