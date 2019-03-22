class Solution:
    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        area = 0 
        for i in range(len(heights)):
            s = h = heights[i]
            for j in range(i+1, len(heights)):
                h = min(h, heights[j])
                s = max(s, (j-i+1)*h)
            area = max(area, s)
        return area
        
    def largestRectangleArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        area = 0
        h_dict = {} 
        for i in range(len(heights)):
            h = heights[i]
            if i==0:
                h_dict[h] = 0
            elif heights[i] < heights[i-1]:
                m = i
                for k in list(h_dict.keys()):
                    if k>=h:
                        s = k * (i-h_dict[k])
                        area = max(area, s)
                        m = min(m, h_dict[k])
                        del h_dict[k]
                h_dict[h] = m

            elif h > heights[i-1]:
                h_dict[h] = i


        l = len(heights)
        for h in h_dict:
            w = h_dict[h]
            s = h*(l-w)
            area = max(area, s)

        return area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        area = 0
        stack = [-1]
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, h*w)
            stack.append(i)

        return area


if __name__ == '__main__':
    solution = Solution()

    heights = [2,1,5,6,2,3,2,2,2] 
    # heights = list(range(50000))
    # heights = [69, 94, 13, 83, 46, 13, 124, 89, 118, 56, 99, 146, 82, 136, 58, 90]
    print(heights)
    ret = solution.largestRectangleArea(heights)
    print(ret)


    # import random
    # for i in range(100):
    #     size = random.randint(0, 1000)
    #     heights = []
    #     for t in range(size):
    #         heights.append(random.randint(1, size*100))
    #     ret = solution.largestRectangleArea(heights)
    #     ret2 = solution.largestRectangleArea2(heights)

    #     if ret != ret2:
    #         print(heights, ret, ret2)
    #         break