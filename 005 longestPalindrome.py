import random


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        max_str = ''
        times = 0;
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                times = times + 1
                if j-i > max_len and s[i:j] == s[i:j][::-1]:
                    max_len = j - i
                    max_str = s[i:j]
        return max_str

    def longestPalindrome2(self, s):
        max_str = ''
        length = len(s)
        times = 0
        for k in range(0, length*2):
            i = k//2
            d = k%2

            start = i - (len(max_str)+1+d)//2
            end = i + (len(max_str)+1+d)//2 + (1-d)

            while start >= 0 and end <= length:
                times = times+1
                if s[start:end:] == s[start:end:][::-1]:
                    max_str = s[start:end:]
                    start = start - 1
                    end = end + 1
                else:
                    break
        # print('>>>>>>>>' ,(len(s), times / len(s), times))
        return (max_str)

    def longestPalindrome3(self, s):
        max_len = 0
        start = 0
        for i in range(len(s)):
            if i-max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len - 1
                max_len += 2
            elif i-max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start+max_len]

if __name__ == '__main__':
    solution = Solution()
    s = 'aaa'
    print(s)
    result = solution.longestPalindrome3(s)
    print((result))

    for i in range(1,11):
        l = 2**i
        # random.randint(1, 20000)
        alphabeta = 'qwertyuiopasdfghjklzxcvbnm'
        s = ''
        for j in range(0,l):
            k = random.randint(0, 25)
            s = s + alphabeta[k]
        print(s)
        print((solution.longestPalindrome(s) ,solution.longestPalindrome2(s), solution.longestPalindrome3(s)))

