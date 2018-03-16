class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0
            
        m = len(grid)
        n = len(grid[0])

        vMap = [[-1]*n for i in range(m)]

        def help(i,j):
            if i==m or j==n:
                return 0
            elif vMap[i][j] != -1:
                return vMap[i][j]
            v = -1
            if i == m-1:
                v = grid[i][j]+help(i,j+1)
            elif j == n-1:
                v = grid[i][j]+help(i+1,j)
            else:
                v = grid[i][j]+min(help(i+1,j), help(i,j+1))
            vMap[i][j] = v
            return v

        help(0,0)

        return vMap[0][0]


    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0
            
        m = len(grid)
        n = len(grid[0])

        vMap = [[0]*(n) for i in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i<m-1 and j<n-1:
                    vMap[i][j] = grid[i][j] + min(vMap[i+1][j],vMap[i][j+1])
                elif i==m-1 and j==n-1:
                    vMap[i][j] = grid[i][j]
                elif i==m-1:
                    vMap[i][j] = grid[i][j] + vMap[i][j+1]
                elif j==n-1:
                    vMap[i][j] = grid[i][j] + vMap[i+1][j]
        for v in vMap:
            print(v)
        return vMap[0][0]



if __name__ == '__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]

    result = solution.minPathSum2(grid)
    print(result)