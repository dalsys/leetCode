class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0
        max_len = 0
        used_char = {}

        for i in range(len(s)):
            if s[i] in used_char:
                start = max(start, used_char[s[i]] + 1)
            used_char[s[i]] = i 
            max_len = max(max_len, i- start + 1)
            print(start, max_len, used_char)

        return max_len

    def lengthOfLongestSubstring2(self, s):

        front = 0
        end = 1
        r_front = 0
        r_end = 1

        if len(s) < 2:
            return len(s)

        while end < len(s):
            ind = s[front:end].find(s[end])
            if ind == -1:
                end = end + 1            
            else:
                if  end - front > r_end - r_front:
                    r_end = end
                    r_front = front

                front = front + ind + 1
                end = end + 1
        if  end - front > r_end - r_front:
            r_end = end
            r_front = front

        return r_end - r_front


if __name__ == '__main__':
    s = 'abbbcabccccabcdabc'
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)

    result2 = solution.lengthOfLongestSubstring2(s)

    print(result,result2)
