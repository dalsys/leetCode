class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # board_dict = {}
        # for i,row in enumerate(board):
        #     for j,l  in enumerate(row):
        #         if l in board_dict:
        #             board_dict[l].add((i,j))
        #         else:
        #             board_dict[l]=set([(i,j)])

        # print(board_dict)

        # ret = set([])

        # for w in word:
        #     if w in board_dict:
        #         pass
        #     else:
        #         return False

        if not board or not board[0] or not word:
            return False
        m,n = len(board), len(board[0])
        k,road,dirs=0,[],[]

        for i in range(m):
            for j in range(n):
                if word[k]==board[i][j]:
                    k+=1
                    road.append((i,j))
                    dirs.append(0)
                    # print(word[k], (i,j),road)
                    prev = 0
                    while 0<k<len(word):
                        (p,q) = road[-1]
                        # print(k, prev, road, dirs)
                        if p-1>=0 and board[p-1][q]==word[k] and prev<1 and not (p-1,q) in road:
                            k+=1
                            p=p-1
                            prev=0
                            road.append((p,q))
                            dirs.append(1)
                        elif q-1>=0 and board[p][q-1]==word[k] and prev<2 and not (p,q-1) in road:
                            k+=1
                            q=q-1
                            prev=0
                            road.append((p,q))
                            dirs.append(2)
                        elif q+1<n and board[p][q+1]==word[k] and prev<3 and not (p,q+1) in road:
                            k+=1
                            q=q+1
                            prev=0
                            road.append((p,q))
                            dirs.append(3)
                        elif p+1<m and board[p+1][q]==word[k] and prev<4 and not (p+1,q) in road:
                            k+=1
                            p=p+1
                            prev=0
                            road.append((p,q))
                            dirs.append(4)
                        else:
                            k-=1
                            road.pop()
                            prev = dirs.pop()
                    if len(road) == len(word):
                        return True
        return False


if __name__ == '__main__':
    solution = Solution()

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = 'ABCB'
    result = solution.exist(board, word)
    print(result)
    a = [1,1,2,3]
    # print(help(list))