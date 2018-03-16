class Solution:
    def searchRange2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            i = nums.index(target)
            n = nums.count(target)
            return [i,i+n-1]
        except:
            return [-1, -1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(nums)-1
        while l<=r and nums[l]<=target<=nums[r] and nums[l]!=nums[r]:
            mid=(l+r)//2
            # print((l, mid, r),nums[l:mid],nums[mid],nums[mid+1:r+1])
            if nums[mid]==target:
                l1,r1 = l, mid-1
                while nums[l1]!=target:
                    mid1 = (l1+r1)//2
                    if nums[mid1]<target:
                        l1 = mid1+1
                    else:
                        r1 = mid1-1

                l2,r2 = mid+1, r
                while nums[r2]!=target:
                    mid2 = (l2+r2)//2
                    if nums[mid2]>target:
                        r2 = mid2-1
                    else:
                        l2 = mid2+1

                # print(l1, r2)

                return [l1,r2]
            elif nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
        # print(l,r)
        if l<=r and nums[l]==nums[r]==target:
            return [l,r]
        else:
            return [-1,-1]



import random
if __name__ == '__main__':
    solution = Solution()

    for t in range(0,400):
        size = random.randint(0,20*t)
        m = random.randint(0,20*t)

        nums=[]
        for i in range(size):
            nums.append(random.randint(0,m))
        nums.sort()
        target = random.randint(0,m)
        # print(nums, target)


        # nums = [ 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
        # print(nums)

        # target = 8

        result = solution.searchRange(nums,target)
        result2 = solution.searchRange2(nums,target)
        # print(result, result2)
        if result!=result2:
            print(">>>>>>>>>>>>>", result, result2 ,nums, target)
        # print()
