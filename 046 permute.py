class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums)<2:
            return [nums]
        else:
            result = []
            for i in nums:
                tmp = nums.copy()
                tmp.remove(i)
                result += [[i]+r for r in self.permute(tmp)]
            return result



if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]

    result = solution.permute(nums)
    print(result)
    # print(dir(nums))
    # nums.remove(1)
    # print(nums)

