class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x > 2147483647:
            return False
        else:
            return str(x) == str(x)[::-1]
        
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t = x
        y = 0
        while t>1:
            y = y*10 + t%10            
            t = t//10

            print(x,y,t)

        return x==y

if __name__ == '__main__':
    solution = Solution()
    x = 21474147412
    result = solution.isPalindrome2(x)
    print(result)        