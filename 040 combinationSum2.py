class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = []
        prev=None
        for i,v in enumerate(candidates):
            if prev==v:
                continue
            prev=v
            if target-v==0:
                ret.append([v])
            elif target-v>0:
                ret += [[v]+x for x in self.combinationSum2(candidates[i+1:], target-v)]
        return ret


if __name__ == '__main__':
    solution = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5,2,3]
    target = 8
    ret = solution.combinationSum2(candidates, target)
    print(ret)

