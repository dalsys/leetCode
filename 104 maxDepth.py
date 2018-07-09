# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode, buildTree

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0



        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1


if __name__ == '__main__':
    solution = Solution()
    li = [2,1,4,None,None,3,6,4,5,6,7,8,1]
    root = buildTree(li)
    print(root)
    ret = solution.maxDepth(root)
    print(ret)        