class Solution:
    def threeSumClosest2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        assert len(nums)>=3
        nums.sort()
        l = len(nums)
        result = float("inf")
        times = 0
        for i in range(l-2):
            for j in range(i+1,l-1):
                for k in range(j+1, l):
                    if abs(nums[i]+nums[j]+nums[k]-target) < abs(result-target):
                        result = nums[i]+nums[j]+nums[k]
        return result

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        assert len(nums)>=3
        nums.sort()
        i,l = 0, len(nums)
        result = sum(nums[0:3])
        while i<len(nums)-2 and result!=target:
            s1 = nums[i]+nums[i+1]+nums[i+2]
            s2 = nums[i]+nums[l-2]+nums[l-1]
            if s1 > target:
                if abs(s1-target) < abs(target-result):
                    result = s1
            elif s2 < target:
                if abs(s2-target) < abs(target-result):
                    result = s2
            else:
                left, right = i+1, l-1
                while left<right and result!=target:
                    s = nums[i]+nums[left]+nums[right]
                    if abs(s-target)<abs(result-target):
                        result = s
                    if s < target:
                        while nums[left]==nums[left+1]:
                            left+=1
                        left+=1
                    else:
                        right-=1
            while i+1<l and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return result

import random
if __name__ == '__main__':
    solution = Solution()
    # nums = [0]*5+[1]*5+[-1]*5
    # nums = list(range(2,15))
    nums = list(range(-2000,2000))
    # nums = []
    # for i in range(100*2**2):
    #     nums.append(random.randint(-10000,10000))
    answer = solution.threeSumClosest(nums,1590)    
    print(answer)
    # print(solution.threeSumClosest2(nums,89590))

