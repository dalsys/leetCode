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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = tmp = ListNode(0)
        curr.next = head
        while head and head.next:
            curr.next = head.next
            n = head.next.next
            head.next.next = head
            head.next = n
            curr = head
            head = head.next
        return tmp.next

        
import random
if __name__ == '__main__':
    # arr=[5, 9, 14,6,2]

    arr=[]
    for i in range(10):
        arr.append(random.randint(0,20))

    print(arr)

    lists = []

    head = d = ListNode(0)
    for a in arr:
        d.next = ListNode(a)
        d = d.next
    head = head.next

    solution = Solution()
    result = solution.swapPairs(head)

    print(result)