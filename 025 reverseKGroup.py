# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        if self.next == None:
            return '{0}'.format(self.val)
        else:
            return '{0}->{1}'.format(self.val, self.next)

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:
            return head
        tmp = curr = ListNode(0)
        curr.next = head

        while head:
            arr = []
            for i in range(k):
                if head:
                    arr.append(head)
                    head = head.next
                else:
                    return tmp.next
            while arr:
                curr.next = arr.pop()
                curr = curr.next
            curr.next = head
        return tmp.next

        
import random
if __name__ == '__main__':
    # arr=[5, 9, 14,6,2]

    arr=[]
    for i in range(100):
        arr.append(random.randint(0,20))

    print(arr)

    lists = []

    head = d = ListNode(0)
    for a in arr:
        d.next = ListNode(a)
        d = d.next
    head = head.next

    solution = Solution()
    result = solution.reverseKGroup(head,3)

    print(result)