import random

class Solution:
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                area = max(area, (j-i)*min(height[i],height[j]))
        return area

    def maxArea3(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        start_max = 0
        end_max = 0
        times = 0
        for i in range(len(height)):
            if height[i]>start_max:
                start_max = height[i]
                end_max = 0
                for j in range(len(height)-1, i, -1):
                    times+=1
                    if height[j]>end_max:
                        end_max = height[j]
                        area = max(area, (j-i)*min(height[i],height[j]))
                        # print(i,j,times)

        print(len(height), times)
        return area

    def maxArea4(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        seq = []
        seq_rev = []
        max_seq = max_seq_rev = 0

        for i in range(len(height)):
            if height[i]>max_seq:
                max_seq = height[i]
                seq.append(i)
            k = len(height) - 1 -i
            if height[k]>max_seq_rev:
                max_seq_rev = height[k]
                seq_rev.append(k)

        q_max = 0
        for p in seq:
            for j in range(q_max,len(seq_rev)):
                q=seq_rev[j]
                area = max(area, (q-p)*min(height[p],height[q]))
                if height[p] <= height[q]:
                    q_max=j
                    break
        return area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height)-1        
        max_height = 0
        while left < right:
            lh = height[left]
            rh = height[right]
            if lh < rh:
                if lh>max_height:
                    area = max(area, (right-left)*lh)
                    max_height = lh
                else:
                    left+=1
            else:
                if rh>max_height:
                    area = max(area, (right-left)*rh)
                    max_height = rh
                else:
                    right-=1
        return area



if __name__ == '__main__':
    solution = Solution()
    height = list(range(1,1000,1))+list(range(1000,0,-1))
    # height = [10, 1, 12, 17, 11, 12, 15, 2, 10, 8, 14, 15, 10, 17, 14, 5, 2]
    # print(height)
    result = solution.maxArea(height)
    print(result)
    # print(solution.maxArea2(height))



 

    # for i in range(1,2000):
    #     l =  random.randint(1, 200)
    #     height = []
    #     for j in range(0,l):
    #         height.append(random.randint(0,2000))
    #     r1 = solution.maxArea(height)
    #     r2 = solution.maxArea2(height)
    #     if r1!=r2:
    #         print('!!!!!!!!!',height, r1, r2)
        # print(len(height), r1, r2, r1 == r2)