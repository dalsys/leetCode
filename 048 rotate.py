class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for i in range(n//2+1):
            for j in range(i, n-i):
                t = matrix[i][j]

                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = t

        
if __name__ == '__main__':
    solution = Solution()
    matrix =[]
    n=5
    for i in range(n):
        matrix.append(list(range(i*n+1, i*n+n+1)))
    for m in matrix:
        print(m)

    solution.rotate(matrix)

    print()

    for m in matrix:
        print(m)
