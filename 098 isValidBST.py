# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return ('TreeNode({0},{1},{2})'.format(self.val,self.left,self.right))

class Solution(object):
    def buildTree(self, li):
        arr = []
        parent = -1
        left = False
        for x in li:
            if parent>= len(arr):
                break
            elif x!=None:
                node=TreeNode(x)
                arr.append(node)
                if parent>=0:
                    if left:
                        arr[parent].left = node
                    else:
                        arr[parent].right = node
            left = (not left)
            if left:
                parent+=1
        if arr:
            return arr[0]
        else:
            return None

    def helper(self, root, min, max):
        if not root:
            return True

        if min < root.val < max:
            left = root.left
            right = root.right
            return self.helper(left, min, root.val) and self.helper(right, root.val, max)
        return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.helper(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    solution = Solution()

    li = [2,1,4,None,None,3,6]

    root = solution.buildTree(li)

    print(root)

    ret = solution.isValidBST(root)
    print(ret)


