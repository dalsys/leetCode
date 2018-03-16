class Solution:
    result_map = {}
    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if self.result_map.get((s,p))!=None:
            return self.result_map.get((s,p))
        # print((s,p))
        result=False
        if len(p)==0:
            result = len(s)==0
        elif p[0]=='?':
            result = len(s)>0 and self.isMatch1(s[1:],p[1:])
        elif p[0]=='*':
            start = 0
            for i in range(0,len(p)):
                if p[i]=='?':
                    start+=1
                elif p[i]!='*': 
                    break
            # print(s, p, i, p[i], start, s[start:])
            if start>len(s):
                result = False
            elif p[i]=='*' or p[i]=='?':
                result = True
            else:
                j = i
                while j<len(p):
                    if p[j]!='*' and p[j]!='?':
                        j+=1
                    else:
                        break

                key=p[i:j]
                # print((i,j), (p[:i], p[i:j],p[j:]))
                while start<len(s):
                    k = s[start:].find(key)
                    if k==-1:
                        result = False
                        break
                    elif self.isMatch1(s[start+k+1:],p[i+1:]):
                        result = True
                        break
                    else:
                        start+=k+1
            # result = self.isMatch1(s,p[1:]) or len(s)>0 and self.isMatch1(s[1:],p)
        else:
            i = 0
            while i<len(s) and i< len(p):
                if p[i]=='?' or p[i]==s[i]:
                    i+=1
                else:
                    break
            # print('......')
            result = i>0 and self.isMatch1(s[i:],p[i:])
        
        self.result_map[(s,p)] = result
        return result

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n = len(s), len(p)
        i,j = 0,0
        last_i, last_j = -1,-1

        while i<m:
            print((i,j), (s,p),last_i)
            if j<n and p[j]=='*':
                while j<n and p[j]=='*':
                    j+=1

                while i<m and (j>=n or p[j]!='?' and s[i]!=p[j]):
                    i+=1

                last_i = i
                last_j = j                                                                                                                                   
                print(i,j)
            elif j<n and (p[j]=='?' or p[j]==s[i]):
                i+=1
                j+=1
            else:
                if last_j == -1:
                    return False
                i = last_i+1
                j = last_j-1

        if j==n or j<n and p[j:]=='*'*(n-j):
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    s = 'abbbbbb'
    p = '*b'

    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # p = "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"
    # s="aaabaaabbababaabbabaababbbbbbaabababbbaabaaaabbbbabbbbaaaaabaabbbbaaaabbabbaaabbabbbababbaaaabbabbabbbbabaabbabbbabbbbabbbbbaabbbababaaaababbbbababababababbabbbbaaaaababbaaababbabaababbbaaabbbbbababab"
    # p="aa*abab*a*a**a*b****ba*ba*aa*****b****b**bbbba*b*b*a**b**b*aab***b*bb***baa*b***a***baa*****a*a*a*ab**a"
    
    result = solution.isMatch(s, p)
    print(result)

    # print(dir(str))

    # for i in solution.result_map:
    #     print((i, solution.result_map[i]))



