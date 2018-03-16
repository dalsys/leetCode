class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return -2147483648
        s = m = nums[0]
        for n in nums[1:]:
            if s<0:
                s = n
            else:
                s += n
            m = max(s, m)
        return m
        
if __name__ == '__main__':
    solution = Solution()
    nums = [-1,-1,-1,-1]
    result = solution.maxSubArray(nums)
    print(result)
