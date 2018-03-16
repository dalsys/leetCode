class Solution:
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        ret = sum(height)
        l,r=0,len(height)-1
        max_height = max(height)
        while height[l]<max_height:
            height[l+1]=max(height[l+1], height[l])
            l+=1
        while height[r]<max_height:
            height[r-1] = max(height[r-1], height[r])
            r-=1
        return sum(height[:l])+max_height*(r-l)+sum(height[r:]) -ret

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        l_max, r_max = 0,0
        ret = 0
        while l<=r:
            if height[l]<height[r]:
                l_max = max(height[l], l_max)
                ret += (l_max-height[l])
                l+=1
            else:
                r_max = max(height[r], r_max)
                ret += (r_max-height[r])
                r-=1
        return ret


        
import random
if __name__ == '__main__':
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    ret = solution.trap(height)
    print(ret)

    # for i in range(1,200):
    #     nums=[]
    #     for j in range(20*i):
    #         nums.append(random.randint(0,40*i))
    #     nums2 = nums.copy()
    #     nums3 = nums.copy()
    #     ret1 = solution.trap(nums)
    #     ret2 = solution.trap2(nums2)
    #     if ret1!=ret2:
    #         print(nums3,ret1,ret2)
