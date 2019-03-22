from ListNode import ListNode, buildCycle

class Solution(object):
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = set([])
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while slow and fast and fast.next:
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    head = buildCycle([0,1,2,3,4,5,6,7,8,9],2)
    ret = solution.hasCycle(head)
    print(ret)
