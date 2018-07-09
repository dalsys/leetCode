class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return ('TreeNode({0},{1},{2})'.format(self.val,self.left,self.right))

def buildTree(li):
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
