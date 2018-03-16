# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        level = [root]

        while level:
            for i in level:
                print(i, end = ' ')
            print()

            for i in range(len(level)//2):
                if level[i] == level[-1-i] == None:
                    continue

                if type(level[i]) != type(level[-1-i]) or level[i].val != level[-1-i].val or type(level[i].left) != type(level[-1-i].right) or type(level[i].right) != type(level[-1-i].left):
                    return False
            nLevel = []
            for l in level:
                if l:
                    nLevel.append(l.left)
                    nLevel.append(l.right)
            level = nLevel

        return True


if __name__ == '__main__':
    print(type(None))

    solution = Solution()
    leaf1 = TreeNode(2)
    leaf1.left = TreeNode(3)
    leaf1.right = None

    leaf2 = TreeNode(2)
    leaf2.left = None
    leaf2.right = TreeNode(3)

    root = TreeNode(1)
    root.left = leaf1
    root.right = leaf2


    # root = [1,2,2,3,4,4,3]
    result = solution.isSymmetric(root)
    print(result)        
        