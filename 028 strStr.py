class Solution:
    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack, needle = 'hello', 'll'
    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)
        
