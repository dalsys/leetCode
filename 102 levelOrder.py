# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode, buildTree

class Solution(object):
    def helper(self, node, level, ret):
        if not node:
            return

        # print(ret, level, node)
        if len(ret)<=level:
            ret.append([])
        ret[level].append(node.val)
        # print(root.val,level)

        self.helper(node.left,level+1, ret)
        self.helper(node.right,level+1, ret)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.helper(root, 0, ret)

        return ret


    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        queue = [(root,0)]
        while queue:
            node, level = queue.pop(0)
            if len(ret)==level:
                ret.append([])
            ret[level].append(node.val)

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return ret


if __name__ == '__main__':
    solution = Solution()
    li = [2,1,4,None,None,3,6,4,5,6,7,8,1]
    root = buildTree(li)
    print(root)
    ret = solution.levelOrder(root)
    print(ret)
    ret2 = solution.levelOrder2(root)
    print(ret2)