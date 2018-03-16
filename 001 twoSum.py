class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}

        for i in range(len(nums)):
            m = nums[i]
            if tmp.get(m) != None:
                return (nums[tmp.get(m)], m)
            else:
                tmp[target-m] = i
        return None;


if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,11,15]
    target = 13
    answer = solution.twoSum(nums, target)
    print(answer)