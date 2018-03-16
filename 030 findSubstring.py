class Solution:
    def findSubstring2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        lens = [len(x) for x in words]
        if len(words)==0 or min(lens)<max(lens):
            return []
        l = lens[0]
        result=[]
        start = 0 
        words.sort()
        while start<len(s)-l*len(words)+1:
            arr = [s[start+l*i:start+l*i+l] for i in range(len(words))]
            arr.sort()
            if arr==words:
                result.append(start)
            start+=1
        return result

    def findSubstring3(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0:
            return []

        ret = []
        strLength = len(s)
        wordLength = len(words[0])
        subStrLength = len(words) * wordLength

        if subStrLength > strLength:
            return []

        # setup times of word in map
        times = {}
        for x in words:
            times[x] = (times.get(x) or 0) + 1

        print(times)

        # not check every char, because we will jump by wordLength
        for start in range(min(wordLength, strLength - subStrLength + 1)):
            print(start)
            match = True
            subStr = s[start:(start + subStrLength)]

            curr = {}
            end = start
            while start + subStrLength <= strLength:
                word = s[end:(end + wordLength)]
                end += wordLength

                if word not in times:
                    # skip this word and restart check (jump to next work)
                    start = end
                    curr.clear()
                else:
                    if word in curr:
                        curr[word] += 1
                    else:
                        curr[word] = 1

                    while curr[word] > times[word]:
                        # if word occurs more then specified times (invalid), then try skip first word until it valid
                        curr[s[start:(start + wordLength)]] -= 1
                        start += wordLength

                    # when stable, if start to end is exactly the length we want, means match
                    if end - start == subStrLength:
                        ret.append(start)
                        print(ret,curr,times)

        return ret

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        lens = [len(x) for x in words]
        if len(words)==0 or min(lens)<max(lens):
            return []

        strLen  = len(s)
        wordNum = len(words)
        wordLen = lens[0]
        wordsLen = wordLen * wordNum
        start = 0
        result = []
        wordDict = {}

        for x in words:
            wordDict[x] = 1 + (wordDict.get(x) or 0)

        print(wordDict)
        curr={}
        for d in range(min(wordLen,strLen-wordsLen+1)):
            print([s[d+i*wordLen:d+(i+1)*wordLen] for i in range((strLen-d)//wordLen) ])
            left,right = d, d + wordsLen
            curr = {}
            print(s[left:right],s[right:strLen])
            while right<=strLen:
                word = s[right-wordLen:right]
                print("word:",word,(left,right))
                if wordDict.get(word):
                    curr[word] = 1+(curr.get(word) or 0)
                    print("curr：",curr)

                    if curr[word] > wordDict[word]:
                        curr.clear()
                        left = right
                        right = left + wordsLen                        
                    elif left==right-wordLen:
                        result.append(left)


                        print(s[left:left+wordLen],s[left+wordsLen:left+wordsLen+wordLen], (left,left+wordsLen) )


                        while s[left:left+wordLen] == s[left+wordsLen:left+wordsLen+wordLen]:
                            left += wordLen
                            result.append(left)
                            print('kkk',s[left:left+wordLen],s[left+wordsLen:left+wordsLen+wordLen], (left,left+wordsLen) )


                        left += wordLen
                        right = left + wordsLen
                        curr.clear()
                        print(result)
                    else:
                        right -= wordLen
                else:
                    left = right
                    right = left+wordsLen
                    curr.clear()



            print()
        return result


        
if __name__ == '__main__':
    s = "ababababa"
    words = ["a","b"]


    solution = Solution()
    result=solution.findSubstring(s, words)
    print(result,[s[i:i+len(words)*len(words[0])] for i in result])

    result2=solution.findSubstring2(s, words)
    print(result2,[s[i:i+len(words)*len(words[0])] for i in result2])
