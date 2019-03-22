class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        pass
        # return self.val
        # return ('{0},{1}'.format(self.val,self.next))
        # return ('ListNode({0},{1})'.format(self.val,self.next))


def buildList(li):
    head = prev = ListNode(0)
    for l in li:
        node = ListNode(l)
        prev.next = node
        prev = node

    return head.next



def buildCycle(li,pos=-1):
    head = prev = ListNode(0)
    for l in li:
        node = ListNode(l)
        prev.next = node
        prev = node

    if -1<pos<len(li):
        tail = head.next
        while pos>0 and tail:
            tail = tail.next
            pos-=1
        prev.next = tail

    return head.next

if __name__ == '__main__':
    pass
    # li = buildList([1,2,3,4],1)
    # i = 0
    # while li and i<10:
    #     print(li.val)
    #     li = li.next
    #     i += 1
    #     pass