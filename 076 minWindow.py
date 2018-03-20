class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_num = {}
        t_inx = {}
        for n in t:
            if n in t_num:
                t_num[n]+=1
            else:
                t_num[n] = 1
                t_inx[n] = []
        ret = ''
        for i, n in enumerate(s):
            if n in t_num:
                if t_num[n]>0:
                    t_num[n]-=1
                    t_inx[n].append(i)
                else:
                    t_inx[n].append(i)
                    t_inx[n] = t_inx[n][1:]

                if sum(t_num.values())==0:
                    l = min([x[0] for x in t_inx.values()])
                    r = max([x[-1] for x in t_inx.values()])
                    if len(ret)==0 or r-l+1<len(ret):
                        ret = s[l:r+1]
            print((i, n), t_num, t_inx.values())

        return ret


    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_num = {}
        for n in t:
            if n in t_num:
                t_num[n]+=1
            else:
                t_num[n]=1
        missing = len(t)
        l,r = 0,0
        k = 0

        for i,n in enumerate(s,1):
            if n in t_num:
                if t_num[n]>0:
                    missing-=1
                t_num[n]-=1

                print((i,n), missing, (l,r), t_num)

                if not missing:
                    while k<i:
                        if s[k] not in t_num:
                            k+=1
                        elif t_num[s[k]]<0:
                            t_num[s[k]]+=1
                            k+=1
                        else:
                            break
                    print((l,r), (k,i))
                    if r==0 or r-l>i-k:
                        l,r = k,i
                        if r-l == len(t):
                            break
        return s[l:r]

if __name__ == '__main__':
    solution = Solution()
    s, t = 'caefgecdaecf', 'cae'
    result = solution.minWindow2(s,t)
    print(result)

    print(help(enumerate))