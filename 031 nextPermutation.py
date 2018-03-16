class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = -1
        l = len(nums)
        for i in range(l-1,0, -1):
            if nums[i-1] < nums[i]:
                p = i-1
                break
        if p!=-1:
            for i in range(l-1, p, -1):
                if nums[i]>nums[p]:
                    t = nums[p]
                    nums[p] = nums[i]
                    nums[i] = t
                    break
        i,j = p+1,l-1
        while i<j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            i+=1
            j-=1


        
if __name__ == '__main__':
    solution = Solution()
    nums = [ 2,3,6,5,4,1]
    solution.nextPermutation(nums)
    print(nums)