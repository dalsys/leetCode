class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        l = len(matrix[0])
        area = 0
        heights = [0]*(l+1)
        for row in matrix:
            for i in list(range(l)):
                if row[i]==0 or row[i]=="0":
                    heights[i]=0
                else:
                    heights[i]+=1
            # area = max(area, self.largestRectangleArea(heights))
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    area = max(area, h*w)
                stack.append(i)

        return area


        
if __name__ == '__main__':
    solution = Solution()

    matrix = []
    m,n = 5,5
    import random
    for i in range(m):
        row = []
        for j in range(n):
            row.append(str(random.randint(0,1)))
        matrix.append(row)
    for row in matrix:
        print(row)

    # matrix = [["0","0","1","0"],
    #           ["1","1","1","0"],
    #           ["0","0","1","0"],
    #           ["0","0","1","0"]]

    ret = solution.maximalRectangle(matrix)
    print(ret)


