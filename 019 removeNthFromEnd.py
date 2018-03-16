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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n <= 0:
            return head
        d = ListNode(0)
        d.next = head
        front = end = d
        for i in range(n+1):
            if front:
                front = front.next 
        while front:
            front = front.next
            end = end.next
        end.next = end.next.next
        return d.next



        # d = ListNode(0) # new dummy head
        # d.next = head
        # first = second = d
        # for i in range(n+1):
        #     first = first.next
        # print(first)
        # while first:
        #     first = first.next
        #     second = second.next
        # print(first, second)
        # second.next = second.next.next
        # return d.next


        return head
if __name__ == '__main__':
    solution = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(head)

    result = solution.removeNthFromEnd(head, 3)
    print(result)