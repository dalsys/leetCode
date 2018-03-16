class Solution:
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        return re.fullmatch(p,s) != None

    result_map = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.result_map={}
        return self.match(s, p)

    def match(self, s, p):

        if self.result_map.get((s,p)) != None:
            return self.result_map.get((s,p))

        result = False
        if len(s)==0:
            if len(p)%2==1:
                result = False
            elif len(p)==0:
                result = True
            elif p[1]=='*':
                result = self.match(s, p[2:])
            else:
                result = False              
        elif len(p)==0:
            result = False
        elif s[0]==p[0] or p[0]=='.':
            if len(p)>1 and p[1] == '*':
                result = self.match(s[1:],p) or self.match(s[1:], p[2:]) or self.match(s, p[2:])
            else:
                result = self.match(s[1:],p[1:])
        elif s[0]!=p[0] and len(p)>1 and p[1]=='*':
            result = self.match(s, p[2:])
        else:
            result = False

        self.result_map[(s,p)] = result

        return result

        
if __name__ == '__main__':
    solution = Solution()
    s = 'aaaaaaaaaaaaab'
    p = 'a*a*a*a*a*a*a*a*a*a*c'

    result = solution.isMatch(s, p)
    result2 = solution.isMatch2(s, p)
    print(result, result2, result == result2)

    # for i in solution.result_map:
    #     print((i, solution.result_map[i]))