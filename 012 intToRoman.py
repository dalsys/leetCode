class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0 or num > 3999:
            return ''
        s = ''
        romanMap = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',5000:''}
        bit = 1000

        while num>0:
            x = num//bit
            if x%5==4:
                s += romanMap[bit] +romanMap[(x+1)*bit]
            else:
                s += romanMap[bit*5]*(x//5) + romanMap[bit]*(x%5)
            num = num%bit
            bit = bit//10
        return s
        

if __name__ == '__main__':
    solution = Solution()
    num = 999
    result = solution.intToRoman(num)
    print(result)