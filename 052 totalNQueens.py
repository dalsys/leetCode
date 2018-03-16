class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[Lista[str]]
        """
        def isSafe(stack, i, v):
            for k in range(i):
                if stack[k] == v or abs(k-i) == abs(stack[k]-v):
                    return False
            return True
        ret = 0
        stack = [0]*n
        i = 0
        while i>=0 and i<n:
            if stack[i]==n:
                i-=1
                stack[i]+=1
                continue
            for j in range(stack[i],n):
                if isSafe(stack, i, j):
                    stack[i] = j
                    if i == n-1:
                        # print('--->', stack)
                        r = ['.'*i+'Q'+'.'*(n-1-i)  for i in stack]
                        ret+=1
                        i-=1
                        stack[i]+=1
                    else:
                        i+=1
                        stack[i]=0
                    break
                elif j == n-1:
                    i-=1
                    stack[i]+=1
        return ret
if __name__ == '__main__':
    solution = Solution()
    for i in range(10):
        result = solution.totalNQueens(i)
        print(result)
