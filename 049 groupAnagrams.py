class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strsDict = {}
        for s in strs:
            key = list(s)
            key.sort()
            key = ''.join(key)

            # print(key,s)
            if strsDict.get(key) == None:
                strsDict[key] = [s]
            else:
                strsDict[key].append(s)
        print(strsDict)
        return [v for k,v in strsDict.items()]     

if __name__ == '__main__':
    solution = Solution()
    strs =[]

    result = solution.groupAnagrams(strs)

    print(result)

