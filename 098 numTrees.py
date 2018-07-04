class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 1
        pack = [1,1]
        for k in list(range(2,n+1)):
            s = 0
            for i in list(range(k)):
                print(pack[i]*pack[k-i-1], end=',')
                s += pack[i]*pack[k-i-1]
            print()
            k+=1
            pack.append(s)

        print(pack)
        return pack[n]


    def numTrees2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 1
        pack = [1]+[0]*n
        for k in list(range(1,n+1)):
            for i in list(range(k//2)):
                pack[k] += pack[i]*pack[k-i-1]
            pack[k]*=2
            if k%2==1:
                i=k//2
                pack[k]+=pack[i]*pack[k-i-1]
            k+=1

        print(pack)
        return pack[n]



if __name__ == '__main__':
    solution = Solution()

    ret = solution.numTrees2(10)
    print(ret)

