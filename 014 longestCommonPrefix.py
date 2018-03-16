class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)


    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        while True:
            for s in strs:
                if len(strs[0])<i+1 or len(s)<i+1 or strs[0][i] != s[i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i] 
        
if __name__ == '__main__':
    solution = Solution()
    strs = []
    result = solution.longestCommonPrefix(strs)
    print(result)
