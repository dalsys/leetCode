class Solution:

    cache = {
        0:[''],
        1:['()']
    }

    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if self.cache.get(n) == None:
            result = set('({})'.format(i) for i in self.generateParenthesis(n-1))
            for i in range(1,n):
                result = result | set(a+b for a in self.generateParenthesis(i) for b in self.generateParenthesis(n-i))
            self.cache[n] = list(result)        
        return self.cache[n]

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [[]for _ in range(n+1)]
        res[0].append('')
        for i in range(1,n+1):
            for j in range(i):
                res[i] += ['({}){}'.format(a,b) for a in res[j] for b in res[i-j-1]]
        return res[n]



if __name__ == '__main__':
    solution = Solution()
    result = solution.generateParenthesis(4)
    print(result)


