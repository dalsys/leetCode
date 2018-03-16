class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums):
            if len(nums)<2:
                return [nums]
            else:
                result = []
                curr = None
                for i in nums:
                    if i == curr:
                        continue
                    curr = i
                    tmp = nums.copy()
                    tmp.remove(i)
                    result += [[i]+r for r in helper(tmp)]
                return result

        nums.sort()
        return helper(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,2]

    result = solution.permuteUnique(nums)
    print(result)
