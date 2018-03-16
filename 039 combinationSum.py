class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        for i,v in enumerate(candidates):
            if target-v==0:
                ret.append([v])
            elif target-v>0:
                ret += [[v]+x for x in self.combinationSum(candidates[i:], target-v)]
        # print(target, ret)
        return ret


if __name__ == '__main__':
    solution = Solution()
    candidates = [1,2,3,7]
    target = 7
    ret = solution.combinationSum(candidates, target)
    print(ret)

