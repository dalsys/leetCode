class Solution:
    def longestConsecutive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()

        print(nums)
        max_len, curr_len = 1,1
        curr = nums[0]
        for n in nums[1:]:
            if n == curr+1:
                curr = n
                curr_len+=1
                max_len = max(max_len, curr_len)
            else:
                curr = n
                curr_len=1
                max_len = max(max_len, curr_len)

        return max_len
        
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        print(nums)
        best = 0
        for x in nums:
            if x+1 not in nums:
                y = x-1
                while y in nums:
                    y -= 1
                best = max(best, x-y)

        return best


if __name__ == '__main__':
    solution = Solution()
    # nums = list(range(1,1000))+list(range(1,-1000,-1))
    nums = [100, 4, 200, 1, 3, 2]
    print(nums)
    ret = solution.longestConsecutive(nums)
    print(ret)

