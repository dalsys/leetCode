class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            chars = [1, s[0]]
            for j in range(1, len(s)):
                # print(j,s[j], chars[-1])
                if s[j] == chars[-1]:
                    chars[-2]+=1
                else:
                    chars.append(1)
                    chars.append(s[j])
            s = ''.join([str(c) for c in chars])
            # print(chars,s)
        return s

        
if __name__ == '__main__':
    solution = Solution()
    n = 5
    ret = solution.countAndSay(n)
    print(ret)