# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next == None:
            return '{0}'.format(self.val)
        else:
            return '{0} {1}'.format(self.val, self.next)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = l1
        n2 = l2
        l3 = n3 = ListNode(0)
        tmp = 0        

        while n1 or n2 or tmp:
            v1, v2 = 0, 0
            if n1:
                v1 = n1.val
                n1 = n1.next
            if n2:
                v2 = n2.val
                n2 = n2.next
            
            v3 = (v1+v2+tmp)%10
            tmp = (v1+v2+tmp)//10

            n3.next = ListNode(v3)
            n3 = n3.next
             

        return l3.next

        
if __name__ == '__main__':
    l1 = ListNode(1)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    l2.next.next.next.next = ListNode(9)
    l2.next.next.next.next.next = ListNode(9)
    l2.next.next.next.next.next.next = ListNode(9)

    print(l1)
    print(l2)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print(result)

    

