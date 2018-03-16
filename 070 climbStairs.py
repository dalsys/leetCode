class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        m = 0
        while m <= n:
            # print(m,n, list(range(1,m+1)), list(range(n-m+1,n+1)), end = ' ')
            p1,p2 = 1,1
            for i in list(range(1,m+1)):
                p1*=i
            for i in list(range(n-m+1,n+1)):
                p2*=i
            # print(p2//p1)
            ret += p2//p1
            m+=1
            n-=1
            pass
        return ret

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 1,1
        for i in range(n):
            a,b = b,a+b 
        return a   
        
if __name__ == '__main__':
    solution = Solution()
    for i in range(100):
        result = solution.climbStairs(i)
        result2 = solution.climbStairs2(i)
        print(i, result, result2)