class Solution:
    
    distDict = {}

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        print(word1, word2)
        if word1 == word2:
            return 0
        elif not word1 or not word2:
            return len(word1)+len(word2)
        elif (word1, word2) in self.distDict:
            return self.distDict[(word1, word2)]
        else:
            i=0            
            while i<len(word1) and i<len(word2) and word1[i] == word2[i]:
                i+=1
            print(word1,word2,i)
            if i==len(word1) or i==len(word2):
                return len(word1)+len(word2)-2*i
            else:
                a = 1+self.minDistance(word1[i+1:], word2[i+1:])
                b = 1+self.minDistance(word1[i:], word2[i+1:])
                c = 1+self.minDistance(word1[i+1:], word2[i:])
                self.distDict[(word1, word2)] = min(a,b,c)
                return self.distDict[(word1, word2)]

if __name__ == '__main__':
    solution = Solution()

    word1, word2 = 'teacher', 'tenace'
    result = solution.minDistance(word1, word2)
    print(result)
    print(solution.distDict)