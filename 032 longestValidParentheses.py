class Solution:
    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        l = 0
        for i,w in enumerate(s):
            if w=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    l = max(l, i-stack[-1])
                else:
                    stack.append(i)
            print(stack)
        return l

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    l = max(i - stack[-1], l)
                else:
                    stack.append(i)
            print(stack,l)
        return l            


if __name__ == '__main__':
    solution = Solution()
    s=")()())()()("
    result = solution.longestValidParentheses2(s)
    print(result)