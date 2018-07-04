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

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None or q==None:
            return p==q
        elif p.val==q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pli=[p]
        qli=[q]
        index = 0

        while index<len(pli):
            if pli[index]==None and qli[index]==None:
                index+=1
            elif pli[index]==None or qli[index]==None:
                return False
            elif pli[index].val!=qli[index].val:
                return False
            else:
                pli.append(pli[index].left)
                pli.append(pli[index].right)
                qli.append(qli[index].left)
                qli.append(qli[index].right)
                index+=1

        return True
if __name__ == '__main__':
    solution = Solution()

    pli = [1,2,3,None,8]
    qli = [1,2,3,None,8,None]

    p = solution.buildTree(pli)
    q = solution.buildTree(qli)

    print(p)
    print(q)

    ret = solution.isSameTree(p, q)
    print(ret)