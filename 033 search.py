class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        if not nums:
            return -1
        length = len(nums)
        l,r = 0, length-1
        while l<=r and nums[l]>=nums[r]:
            mid = (l+r)//2
            # print((l,mid,r), nums[l:mid],nums[mid],nums[mid+1:r+1])

            if mid+1<length and nums[mid]>nums[mid+1]:
                r = mid
                break
            elif nums[mid]>nums[0]:
                l=mid+1
            elif nums[mid]<nums[0]:
                r=mid-1
            else: 
                break

        l = r-length+1

        # print(l,r)

        if target>nums[r] or target<nums[l]:
            return -1
        elif nums[0]>target:
            l+=length
            r=length-1
        else:
            l=0

        # print(nums[:r+1],nums[r+1:])

        # print((l,r), (nums[l], nums[r]))

        while l<=r:
            mid = (l+r)//2
            # print(mid,nums[mid], l,r)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1


    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            return -1

    def search3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l,r = 0, len(nums)-1
        while l<=r:
            mid=(l+r)//2
            # print((l, mid, r),nums[l:mid],nums[mid],nums[mid+1:r+1])
            # print()

            if nums[mid]==target:
                return mid
            elif l==mid:
                if nums[r]==target:
                    return r
                else:
                    return -1
            elif nums[mid]<target:
                if nums[mid+1]<=nums[r] and target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]>target:
                if  nums[l]<=nums[mid-1] and target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

import random        
if __name__ == '__main__':
    solution = Solution()

    for t in range(1000):
        size = random.randint(0,20*t)
        m = random.randint(0,20*t)

        nums=[]
        for i in range(size):
            nums.append(random.randint(0,m))
        nums = list(set(nums))
        nums.sort()
        d = random.randint(0,len(nums))
        nums = nums[d:]+nums[:d]
        target = random.randint(0,m)
        # print(nums, target)


        # nums = [432, 2]
        # print(nums)

        # target = 2

        result = solution.search(nums,target)
        result2 = solution.search2(nums,target)
        result3 = solution.search3(nums,target)
        if result3 != result2:
            print(">>>>>>>>>>>>>",result , result2, result3, nums, target)
        # print()
