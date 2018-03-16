class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
        return l


import random

if __name__ == '__main__':
    solution = Solution()

    for t in range(100):
        size = random.randint(0,20*t)
        m = random.randint(0,20*t)

        nums=[]
        for i in range(size):
            nums.append(random.randint(0,m))
        nums = list(set(nums))
        nums.sort()
        target = random.randint(0,m)
        # print(nums, target)


        # nums = [0, 2, 4, 5, 7, 10, 13, 15, 16, 18, 21, 22, 24, 26, 27, 31, 33, 34, 40, 45, 47, 50, 52, 55, 56, 57, 58, 60, 63, 65, 66, 68, 69, 72, 74, 76, 79, 80, 82, 83, 84]

        # target = 37
        # print(nums, target)

        result = solution.searchInsert(nums,target)
        if result < len(nums) and not (nums[result]==target or nums[result-1]<target<nums[result] or result==0):
            print(">>>>>>>>>>>>>", result ,nums, target)
            print(nums[result]==target, nums[result-1]<target<nums[result], (nums[result-1],target,nums[result]))
        # print()