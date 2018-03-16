# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        if self.next == None:
            return '{0}'.format(self.val)
        else:
            return '{0},{1}'.format(self.val, self.next)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print('[{}],[{}]'.format(l1,l2))
        d = ListNode(0)
        head = d
        while l1 or l2:
            if not l2 or l1.val <= l2.val:
                d.next = l1
                d = d.next
                l1 = l1.next
            else:
                d.next = l2
                d = d.next
                l2 = l2.next
        return head.next

if __name__ == '__main__':
    solution = Solution()
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(8)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    m1 = ListNode(1)
    m2 = ListNode(2)
    m3 = ListNode(4)
    m4 = ListNode(6)
    m1.next = m2
    m2.next = m3
    m3.next = m4



    result = solution.mergeTwoLists(n1,m1)
    print(result)