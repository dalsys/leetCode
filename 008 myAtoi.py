import re

class Solution:
    def myAtoi(self, s):
        """
        :type str: s
        :rtype: int
        """
        s, n = s.strip(), ''
        for x in s:
            if x >= '0' and x < 'a':
                n += x
            elif len(n)==0 and (x=='-' or x=='+'):
                n += x
                n += '0'
            else:
                break
        n = 0 if len(n)==0 else int(n)
        if n>2147483647:
            return 2147483647
        elif n < -2147483648:
            return -2147483648
        else:
            return n

    def myAtoi2(self, s):
        try:
            n = re.match(r'^\s*[+-]?\d+',s).group()
            n = int(n)
            if n>2147483647:
                return 2147483647
            elif n < -2147483648:
                return -2147483648
            else:
                return n            
        except Exception as e:
            return 0


if __name__ == '__main__':
    solution = Solution()
    s = '        -90'
    result = solution.myAtoi(s)
    print(result, solution.myAtoi2(s))