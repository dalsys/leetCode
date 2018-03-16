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
        

if __name__ == '__main__':
    solution = Solution()
    x = 21474147412
    result = solution.isPalindrome(x)
    print(result)        