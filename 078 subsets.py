class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sets = [[]]
        for i in nums:
            sets_copy = []
            for s in sets:
                t = s.copy()
                t.append(i)
                sets_copy.append(t)
            sets+=sets_copy
        return sets



if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    result = solution.subsets(nums)
    print(result)