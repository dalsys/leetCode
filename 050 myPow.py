class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return pow(x,n)
        sign = n
        n = abs(n)
        ret = 1
        i,p = 1, x
        while n!=0:
            print(ret,n)
            ret*=p
            n-=i
            if i*2<=n:
                i*=2
                p*=p
            else:
                i,p=1,x

        if sign >= 0:
            return ret
        else:
            return 1/ret
        

if __name__ == '__main__':
    solution = Solution()
    x = 2.3
    n = 10

    result = solution.myPow(x, n)
    print(result, pow(x,n))

