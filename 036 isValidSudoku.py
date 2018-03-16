class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(s):
            tmp={}
            for k in s:
                if k!='.':
                    if tmp.get(k):
                        return False
                    tmp[k]=1
            return True

        for i in range(9):
            m,n = i//3*3,i%3*3            
            row=board[i]
            col=[row[i] for row in board]
            box=[board[j][k] for j in range(m,m+3) for k in range(n,n+3)]
            
            if not isValid(row) or not isValid(col) or not isValid(box):
                return False
        return True

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += (c,j),(i,c),(i//3,j//3,c),
        print(seen)
        return len(seen) == len(set(seen))



        
if __name__ == '__main__':
    solution = Solution()
    board = [[".","8","7","6","5","4","3","2","1"],
             ["2",".",".",".",".",".",".",".","."],
             ["3",".","2",".",".",".",".",".","."],
             ["4",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".",".","."],
             ["6",".",".",".",".",".",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             ["8",".",".",".",".",".",".",".","."],
             ["9",".",".",".",".",".",".",".","."]]
    result = solution.isValidSudoku(board)
    print(result)
