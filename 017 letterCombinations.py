class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        digitsMap = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

        for d in digits:
            if int(d)>1:
                result = self.combination(digitsMap[int(d)], result)
            else:
                return []
        return result
            
    def combination(self, chars, letters):
        result = []
        if len(letters)==0:
            letters.append('')
        for s in letters:
            for c in chars:
                result.append(s+c)
        return result


if __name__ == '__main__':
    solution = Solution()
    digits = '23'
    result = solution.letterCombinations(digits)
    print(result)
