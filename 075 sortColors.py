class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print(nums)
        l,r = 0, len(nums)-1
        for i in nums:
            if i==0:
                l+=1
            elif i==2:
                r-=1
        for i in range(l):
            nums[i]=0
        for i in range(l,r):
            nums[i]=1
        for i in range(r,len(nums)):
            nums[i]=2
if __name__ == '__main__':
    solution = Solution()
    nums = [1,0,2,0,0,0,1]
    solution.sortColors(nums)
    print(nums)