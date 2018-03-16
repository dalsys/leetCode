class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1 or numRows >= len(s):
            return s
        s_new = ''
        # print(len(s)//(numRows*2-2)+1, len(s))
        for i in range(numRows):
            for j in range(len(s)//(numRows*2-2)+1):

                s_tmp = s[j*2*(numRows-1):(j+1)*2*(numRows-1)]

                if i < len(s_tmp):
                    s_new += s_tmp[i]
                    # print(s_tmp[i], end=',')
                if i < numRows-1 and (numRows-1)*2-i < len(s_tmp):
                    s_new += s_tmp[(numRows-1)*2-i]
                    # print(s_tmp[(numRows-1)*2-i], end=',')

        return s_new

    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1 or numRows >= len(s):   
            return s
        s_new = ''
        for i in range(numRows):
            if i==0 or i == numRows-1:
                s_new+=s[i::numRows*2-2]
            else:
                l1 = s[i::numRows*2-2]
                l2 = s[numRows*2-2-i::numRows*2-2]
                l = ''
                for j in range(len(l1)):
                    l+=l1[j]
                    if j < len(l2):
                        l+=l2[j]
                s_new+=l
        return s_new

    def convert3(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index+=step

        return ''.join(L)

        
if __name__ == '__main__':
    s = '0123456789abcdef'
    solution = Solution()
    result = solution.convert(s, 3)
    result2 = solution.convert2(s, 3)
    result3 = solution.convert3(s, 3)
    print(result==result3,result,result2,result3)
