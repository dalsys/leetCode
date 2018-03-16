class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def help(nums):
            ret = 1
            for i in nums:
                ret *= i
            return ret

        m, n = max(m, n), min(m,n)
        a=list(range(1,n))
        b=list(range(m,m+n-1))
        return help(b)//help(a)



if __name__ == '__main__':
    solution = Solution()
    m = 0
    n = 0
    result = solution.uniquePaths(m, n)
    print(result)