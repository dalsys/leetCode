# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode, buildTree

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_path = float('-inf')
        def calPath(root):
            nonlocal max_path
            if not root:
                return 0
            else:
                left = max(calPath(root.left), 0)
                right = max(calPath(root.right), 0)
                s_root = root.val + right + left
                max_path = max(max_path, s_root)
                return root.val + max(left, right)
        calPath(root)
        return max_path

if __name__ == '__main__':
    solution = Solution()
    li = [2,1,4,None,None,3,6,4,5,6,7,-8,1]
    root = buildTree(li)
    print(root)
    ret = solution.maxPathSum(root)
    print(ret)