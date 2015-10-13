class Solution(object):
    def validateList(self, ls):
        dots = ls.count('.')
        nums = 9-dots
        sl = set(ls)
        # print len(ls), nums
        if len(sl) == nums +1:
            return True
        return False
    
    def isValidSudoku(self, board):
        columns = [['' for x in range(len(board))] for y in range(len(board))]
        b1 = []
        b2 = []
        b3 = []
        for i in range(len(board)):
            # for j in range(len(board)):
            if not self.validateList(board[i]):
                print "invalid row"
                return False
            b1.extend(board[i][0:3])
            b2.extend(board[i][3:6])
            b3.extend(board[i][6:9])
            if (i+1)%3 == 0:
                print "into boards"
                if not self.validateList(b1) or not self.validateList(b2) or not self.validateList(b3):
                    print "invalid small board"
                    return False
                b1 = []
                b2 = []
                b3 = []
            
            for j in range(len(board)):
                columns[j][i] = board[i][j]
        for i in range(len(columns)):
            if not self.validateList(columns[i]):
                print "invalid columns"
                return False
        return True
                
                
                
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
