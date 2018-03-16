from itertools import combinations
from collections import defaultdict, Counter

class Solution:
    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        result = []
        for i in range(0,len(nums)-4):
            for j in range(i+1,len(nums)-3):
                for k in range(j+1,len(nums)-2):
                    for l in range(k+1,len(nums)-1):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            result.append([nums[i],nums[j],nums[k],nums[l]])
        return result

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        # print(nums)
        result = []
        i,l = 0,len(nums)

        times = 0

        while i<l-3:
            if sum(nums[i:i+4])>target:
                print('OVER',i, nums[i:i+4])
                print(times)
                return result
            if nums[i]+sum(nums[l-3:l])<target:
                i+=1
                continue

            j = i+1
            while j<l-2:
                
                if nums[i]+sum(nums[j:j+3])>target or nums[i]+nums[j]+sum(nums[l-2:l])<target:
                    j+=1
                    continue
                left, right = j+1, l-1
                t = target-nums[i]-nums[j]


                # print((i,j),nums[i],nums[j],nums[left:right+1])
                
                while left < right:
                    times+=1
                    if nums[left]+nums[right]<t:
                        while left+1<right and nums[left]==nums[left+1]:
                            left+=1
                        left+=1
                    elif nums[left]+nums[right]>t:
                        while right-1>left and nums[right]==nums[right-1]:
                            right-=1
                        right-=1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left+1<right and nums[left]==nums[left+1]:
                            left+=1
                        while right-1>left and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1


                while j+1<l and nums[j]==nums[j+1]:
                    j+=1
                j+=1

            while i+1<l and nums[i]==nums[i+1]:
                i+=1
            i+=1
            # print()
        print(times)
        return result




    def fourSum3(self, nums, target):
        if len(nums) < 4:
            return []
        half_target = target // 2
        counter = Counter(nums)
        uniques_wide = sorted(counter)
        x_min, x_max = target - 3 * uniques_wide[-1], target - 3 * uniques_wide[0] # suboptimal
        uniques = [ x for x in uniques_wide if x_min <= x <= x_max ]
        duplicates = [x for x in uniques if counter[x] > 1]
        target_minus_xy_sums = set(target - x - y for x, y in combinations(uniques, 2))
        target_minus_xy_sums |= set(target - x - x for x in duplicates)
        ab_sum_pairs, cd_sum_pairs = defaultdict(list), defaultdict(list)
        for (x, y) in combinations(uniques, 2):
            if x + y in target_minus_xy_sums:
                if x + y <= half_target:
                    ab_sum_pairs[x + y].append((x, y))
                if x + y >= half_target:
                    cd_sum_pairs[x + y].append((x, y))
        for x in duplicates:
            if x + x in target_minus_xy_sums:
                if x + x <= half_target:
                    ab_sum_pairs[x + x].append((x, x))
                if x + x >= half_target:
                    cd_sum_pairs[x + x].append((x, x))
        return [[a, b, c, d]
                for ab in ab_sum_pairs
                for (a, b) in ab_sum_pairs[ab]
                for (c, d) in cd_sum_pairs[target - ab]
                if b < c or b == c and int(a == b) + int(d == b) + 2 <= counter[b]]



import random
if __name__ == '__main__':
    solution = Solution()
    target = 19
    # nums = [0]*50+[1]*5+[-1]*5
    nums = [5, -3, 2, 7, -9, 3, 6, -6, 0, -8,4,3,4,3,0,5,5]
    # nums = list(range(-200,200))
    # nums=[]
    # for i in range(1000*2**1):
    #     nums.append(random.randint(-10000,10000))
    # print(nums)
    answer = solution.fourSum3(nums,target)
    print(answer)

