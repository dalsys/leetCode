class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,j=0,len(nums)-1
        while i<=j:
            if nums[i]==val:
                nums[i]=nums[j]
                nums[j]=val
                j-=1
            else:
                i+=1
            # print((i,j),nums)
        # print(i,j)
        return i

import random
if __name__ == '__main__':
    for j in range(5):
        # nums=[2,3,3,3]
        # val = 0
        nums=[]
        for i in range(10*2**j) :#range(random.randint(0,50000))
            nums.append(random.randint(0,10*2**j))
        val = random.randint(0,10*2**j)

        print(nums,val)

        solution = Solution()
        result = solution.removeElement(nums, val)
        # if nums.count(val) != len(nums)-result:
        #     print('!!!!!!!!!!!!!!!!!!!!!')
        print(nums[:result], (nums.count(val) , len(nums)-result))
        print()