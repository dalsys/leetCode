# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import ListNode, buildCycle

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while slow and fast and fast.next:
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                i=0
                fast = head
                while fast!=slow:
                    slow = slow.next
                    fast = fast.next
                    i+=1
                return i
        return None


if __name__ == '__main__':
    solution = Solution()
    li = [0,1,2,3,4,5,6,7,8,9]
    pos = 0
    head = buildCycle(li, pos)
    ret = solution.detectCycle(head)
    print(ret)        