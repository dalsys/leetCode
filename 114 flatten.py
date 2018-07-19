# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode, buildTree

class Solution:
    def flatten2(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 

        self.flatten2(root.left)
        self.flatten2(root.right)

        if root.left:
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None

    def helper(self, root):
        if root.left and root.right:
            left_head, left_tail = self.helper(root.left)
            right_head, right_tail = self.helper(root.right)
            
            root.left = None
            root.right = left_head
            left_tail.right = right_head

            return (root, right_tail)
        elif root.left:
            left_head, left_tail = self.helper(root.left)

            root.left = None
            root.right = left_head

            return (root, left_tail)
        elif root.right:
            right_head, right_tail = self.helper(root.right)

            return (root, right_tail)
        else:
            return (root, root)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.helper(root)



         

if __name__ == '__main__':
    solution = Solution()
    li = [1,2]
    # li = [2,1,4,None,None,3,6,4,5,6,7,8,1]
    # li = [1,2,3]
    root = buildTree(li)
    print(root)
    solution.flatten(root)
    print(root)