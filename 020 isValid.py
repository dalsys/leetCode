class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracketMap = {'(':')','[':']','{':'}'}
        for c in s:
            if bracketMap.get(c):
                stack.append(c)
            elif not stack or bracketMap.get(stack.pop()) != c:
                return False
        return not stack


if __name__ == '__main__':
    solution = Solution()
    s = '[[[[[[{}{()}]]]]]]'
    result = solution.isValid(s)
    print(result)
        