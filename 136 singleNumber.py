class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for n in nums:
            s = s^n
        return s

        
if __name__ == '__main__':
    solution = Solution()
    nums = list(range(1,13))+list(range(1,11))
    print(nums)
    ret = solution.singleNumber(nums)
    print(ret)
