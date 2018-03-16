class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        nums.sort()
        for i,n in enumerate(nums):
            if n<=ret:
                continue
            if n==ret+1:
                ret+=1
            else:
                return ret+1
        return ret+1

        
import random
if __name__ == '__main__':
    solution = Solution()
    nums = [3,4,-1,1]
    ret = solution.firstMissingPositive(nums)
    print(ret)

