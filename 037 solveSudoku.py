class Solution:

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += (c,j),(i,c),(i//3,j//3,c),
        return len(seen) == len(set(seen))

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows,cols,boxes=[set(range(1,10)) for _ in range(9)],[set(range(1,10)) for _ in range(9)],[set(range(1,10)) for _ in range(9)]
        empty,buff = [],{}

        for i in range(9):
            for j in range(9):
                k = board[i][j]
                if k!='.':
                    k=int(k)
                    rows[i].remove(k)
                    cols[j].remove(k)
                    boxes[i//3*3+j//3].remove(k)
                else:
                    empty.append((i,j))
                    buff[(i,j)]=0                    

        # print(rows)
        # print(cols)
        # print(boxes)
        # print(empty)

        p=0
        while p<len(empty):
            (i,j) = empty[p]                                     
            n = board[i][j]
            if n!='.':
                n=int(n)
                rows[i].add(n)
                cols[j].add(n)
                boxes[i//3*3+j//3].add(n)
            s = list(rows[i].intersection(cols[j]).intersection(boxes[i//3*3+j//3]))
            s.sort()
            
            # print(p, (i,j), buff[(i,j)], len(s)>buff[(i,j)],s, buff[(0,0)])
            
            if len(s)>buff[(i,j)]:
                v=s[buff[(i,j)]]
                board[i][j]=str(v)
                buff[(i,j)]+=1
                rows[i].remove(v)
                cols[j].remove(v)
                boxes[i//3*3+j//3].remove(v)
                p+=1
            else:
                buff[(i,j)]=0
                board[i][j]='.'
                p-=1
                if p<0:
                    return
                # print()
                # for row in board:
                #     print(row)


if __name__ == '__main__':
    solution = Solution()
    board1 = [[".",".","9","7","4","8",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             [".","2",".","1",".","9",".",".","."],
             [".",".","7",".",".",".","2","4","."],
             [".","6","4",".","1",".","5","9","."],
             [".","9","8",".",".",".","3",".","."],
             [".",".",".","8",".","3",".","2","."],
             [".",".",".",".",".",".",".",".","6"],
             [".",".",".","2","7","5","9",".","1"]]
    board2 = [[".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]
    board3 = [[".","2","6","5",".",".",".","9","."],
             ["5",".",".",".","7","9",".",".","4"],
             ["3",".",".",".","1",".",".",".","."],
             ["6",".",".",".",".",".","8",".","7"],
             [".","7","5",".","2",".",".","1","."],
             [".","1",".",".",".",".","4",".","."],
             [".",".",".","3",".","8","9",".","2"],
             ["7",".",".",".","6",".",".","4","."],
             [".","3",".","2",".",".","1",".","."]]

    board4 = [[".",".","5","3",".",".",".",".","."],
             ["8",".",".",".",".",".",".","2","."],
             [".","7",".",".","1",".","5",".","."],
             ["4",".",".",".",".","5","3",".","."],
             [".","1",".",".","7",".",".",".","6"],
             [".",".","3","2",".",".",".","8","."],
             [".","6",".","5",".",".",".",".","9"],
             [".",".","4",".",".",".",".","3","."],
             [".",".",".",".",".","9","7",".","."]]

    board = board4

    solution.solveSudoku(board)
    for row in board:
        print(row)

    print(solution.isValidSudoku(board))
