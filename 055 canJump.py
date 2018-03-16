class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last=0
        for i in range(0, len(nums)):
            print(nums[i:],last)
            if i > last:
                return False
            elif last>=len(nums)-1:
                return True
            else:
                last = max(last, nums[i] + i)
if __name__ == '__main__':
    solution = Solution()
    nums =  [10,1]  #[2,3,1,1,4]
    result = solution.canJump(nums)
    print(result)