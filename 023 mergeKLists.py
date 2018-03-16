# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # def __str__(self):
    #     if self.next == None:
    #         return '{0}'.format(self.val)
    #     else:
    #         return '{0} {1}'.format(self.val, self.next)

class Solution:
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = d = ListNode(0)
        times = 0
        while d:
            m = -1
            for i in range(len(lists)):
                times+=1
                if lists[i] and (m<0 or lists[i].val < lists[m].val):
                    m = i
            if m>=0:
                d.next = lists[m]
                if lists[m]:
                    lists[m] = lists[m].next
            d = d.next
        print(times)
        return head.next
        
    def mergeKLists3(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length<3:
            l1 = lists[0] if length>=1 else []
            l2 = lists[1] if length>=2 else []
            return self.mergeTwoLists(l1, l2)
        else:
            return self.mergeKLists([self.mergeKLists(lists[:length//2]), self.mergeKLists(lists[length//2:length])])

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = curr = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        print(curr.val, tmp.next)
        return tmp.next


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr = []
        for li in lists:
            while li:
                arr.append(li.val)
                li = li.next
        arr.sort()
        head = curr = ListNode(0)
        for i in range(len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return head.next        

import random
if __name__ == '__main__':
    arr=[]
    for i in range(20):
        ar = []
        for j in range(10):
            ar.append(random.randint(0,20))
        ar.sort()
        arr.append(ar)

    print(arr)

    lists = []
    for ar in arr:
        head = d = ListNode(0)
        for a in ar:
            d.next = ListNode(a)
            d = d.next
        lists.append(head.next)

    solution = Solution()
    result = solution.mergeKLists3(lists)

    tmp = result
    while tmp:
        print(tmp.val, end=', ')
        tmp = tmp.next
        pass


