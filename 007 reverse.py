class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        x = x*sign
        k = 0
        if x >2**31-1:
            return 0
        while x > 0 :
            k = k*10 + x%10
            x = x//10
        return 0 if k >2**31-1 else k*sign


    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        x *= sign
        k = int(str(x)[::-1])
        return 0 if x>2147483647 or k > 2147483647 else k * sign

        
if __name__ == '__main__':
    x = -2147447412
    solution = Solution()
    result = solution.reverse(x)
    print(result,solution.reverse2(x))
