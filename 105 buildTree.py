# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder)!=len(inorder):
            return None

        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        node.left = self.buildTree2(preorder[1: index+1], inorder[:index])
        node.right = self.buildTree2(preorder[index+1:], inorder[index+1:])
        return node

    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder)!=len(inorder):
            return None

        lookup = {v:i for i,v in enumerate(inorder)}

        def build(p1, q1, p2, q2):
            # print(preorder[p1:q1], inorder[p2:q2], (p1,q1), (p2,q2))
            if p1==q1:
                return None

            m = lookup[preorder[p1]]
            node = TreeNode(preorder[p1])
            node.left = build(p1+1, p1+1+(m-p2), p2, m)
            node.right = build(p1+1+(m-p2), q1, m+1, q2)
            return node

        return build(0, len(preorder), 0, len(inorder))




if __name__ == '__main__':
    solution = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    ret = solution.buildTree(preorder, inorder)
    print(ret)

    ret2 = solution.buildTree2(preorder, inorder)
    print(ret2)