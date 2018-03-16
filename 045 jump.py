class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        
        target = len(nums)-1
        length=0

        i = 0
        while i<len(nums) and i+nums[i]<target:
            print(i,nums[i], i+nums[i]<target)
            max_range=0
            for j in range(i+1, i+nums[i]+1):
                print(j)
                if j>len(nums) or j+nums[j]>=target:
                    i = j
                    break
                elif j+nums[j] > max_range:
                        max_range = j+nums[j] 
                        i = j   
            print('j:',j, ',i:', i)  
            print()            
            length+=1

        return length+1
        

if __name__ == '__main__':
    solution = Solution()
    nums = [2,1]

    result = solution.jump(nums)
    print(result)
