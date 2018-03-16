class Solution:
    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend>2147483647 or dividend<-2147483647 or divisor>2147483647 or divisor<-2147483647:
            return 2147483647
        elif divisor==0:
            return None
        elif divisor==1:
            return dividend
        elif divisor==-1:
            return min(0-dividend, 2147483647)
        else:
            sign = 1 
            if (dividend>0)!=(divisor>0):
                sign = -1
            if dividend<=0:
                dividend=0-dividend
            if divisor<=0:
                divisor=0-divisor
            result = 0
            t = 1
            tmp=[(t,divisor)]
            while divisor<dividend:
                t=t+t
                divisor=divisor+divisor
                tmp.append((t,divisor))
            i = len(tmp)-2
            while i>=0 and dividend>0:
                print(i, tmp[i])
                if dividend>=tmp[i][1]:
                    dividend-=tmp[i][1]
                    result+=tmp[i][0]
                i-=1
            if sign==-1:
                result=0-result
            return result

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return None
        sign = (dividend>0)==(divisor>0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while divisor <= dividend:
            d, r = divisor, 1
            while d <= dividend:
                dividend -= d
                result += r
                d <<= 1
                r <<= 1
        if not sign:
            result = -result
        return min(max(result, -2147483648), 2147483647)





if __name__ == '__main__':
    dividend = 0
    divisor = 1

    solution = Solution()
    result=solution.divide(dividend, divisor)
    print(result, dividend//divisor)
        