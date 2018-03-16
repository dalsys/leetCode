class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def add(num1, num2, delta):
            print((num1, num2,'0'*delta))
            # print(num1[-delta:], '0'*(delta-len(num1)))
            num1='0'+num1
            num2='0'+num2
            i,j = max(len(num1)-1-delta, 0), len(num2)-1
            s,t = [num1[len(num1)-delta:][::-1]+'0'*(delta-len(num1))] ,0
            print(num1[len(num1)-delta:][::-1], '0'*(delta-len(num1)))
            while (i>0 and j>0) or t>0:
                k = int(num1[i])+int(num2[j])+t
                s.append(str(k%10))
                t = k//10
                if i>0:
                    i-=1
                if j>0:
                    j-=1
            if i>0:
                s.append(num1[1:i+1][::-1])
            if j>0:
                s.append(num2[1:j+1][::-1])

            print(s,''.join(s)[::-1])
            return ''.join(s)[::-1]

        print(add('41', '1', 4))
        return

        product='0'
        multipy_dict = {'0':'0','1':num2}
        for i,m in enumerate(num1[::-1]):
            if not multipy_dict.get(m):
                t='0'
                for j,n in enumerate(num2[::-1]):
                    t = add(t, str(int(m)*int(n)), j)
                multipy_dict[m] = t

            if multipy_dict[m]!='0':
                product = add(product, multipy_dict[m], i)
                print(product)

            # print(product)
        return product

import random
        
if __name__ == '__main__':
    solution = Solution()
    for i in range(0,1):
        # num1, num2 = str(random.randint(1,9)),str(random.randint(1,9))
        # for j in range(random.randint(0,i*10)):
        #     num1 += str(random.randint(0,9))
        # for j in range(random.randint(0,i*10)):
        #     num2 += str(random.randint(0,9))
        num1 = "61746864938910049"
        num2 = "1"
        ret = solution.multiply(num1,num2)
        # print(ret)
        # if int(ret)!=int(num1)*int(num2):
        #     print(num1, num2, ret, str(int(num1)*int(num2)))


# 61746864938910049 1 61746864900000309 61746864938910049
