class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, ret = float('inf'), 0
        for p in prices:
            if p<buy:
                buy = p
            else:
                ret = max(ret, p-buy)
        return ret

if __name__ == '__main__':
    solution = Solution()
    prices = [7,1,5,3,6,4,0,8]
    # prices = [2,1,4,3,6,4,5,6,7,8,1]
    # prices = [1,2,3]
    print(prices)
    ret = solution.maxProfit(prices)
    print(ret)