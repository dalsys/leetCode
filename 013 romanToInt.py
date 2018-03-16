from intToRoman import Solution as itr

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        i,length=0,len(s)
        while i<length:
            if romanMap.get(s[i]):
                if i+1<length and romanMap.get(s[i+1]) and romanMap.get(s[i])<romanMap.get(s[i+1]):
                    num-=romanMap[s[i]]
                else:
                    num+=romanMap[s[i]]
            i+=1
        return num 


if __name__ == '__main__':
    solution = Solution()
    for num in range(3999):
        s = itr.intToRoman(itr, num)
        result = solution.romanToInt(s)
        if result!=num:
            print(result, num, result==num, s)