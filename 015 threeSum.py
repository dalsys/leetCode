class Solution:
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        tmp = {}
        for i in range(len(nums)-2):
            n = nums[i]
            if not tmp.get(n):
                tmp[n] = True
                for r in self.twoSum(nums[i+1:], -nums[i]):
                    r.append(nums[i])
                    r.sort()
                    result.add(tuple(r))
            pass
        return list(map(list, result))



    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        result = []
        for i in range(len(nums)):
            m = nums[i]
            if tmp.get(m) != None:
                result.append([nums[tmp.get(m)], m])
            else:
                tmp[target-m] = i
        return result;

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        start,end = 0,len(nums)-1
        while start+1<end:
            if start>0 and nums[start]==nums[start-1]:
                start+=1
                continue
            if nums[start]+nums[start+1]+nums[end]>0:
                end -= 1
            elif nums[start]+nums[end-1]+nums[end]<0:
                start +=1
            else:
                l, r = start+1, end
                k=0
                while l<r:
                    if l>start+1 and nums[l-1]==nums[l]:
                        l+=1
                        continue
                    s = nums[start]+nums[l]+nums[r]
                    if s>0:
                        r-=1
                    elif s<0:
                        l+=1
                    else:
                        result.append([nums[start],nums[l],nums[r]])
                        l+=1
                        r-=1
                start+=1
        return result



import random
if __name__ == '__main__':
    solution = Solution()
    nums = [0]*50+[1]*5+[-1]*5
    # nums = [5, -3, 2, 7, -9, 3, 6, -6, 0, -8, 0,0,19,20,30,17]
    # nums = list(range(-2000,2000))
    # for i in range(1000*2**1):
    #     nums.append(random.randint(-10000,10000))
    answer = solution.threeSum(nums)
    print(answer)
