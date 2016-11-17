https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d = {}
        temp = head
        max = 0
        if temp.next == None and n == 1:
            return []
        
        while temp:
          max += 1
            d[max] = temp
            temp = temp.next
      
        n -= 1
        if max-n > 1:
            node = d[max-n-1]
            node.next = node.next.next
        
        elif max - n == 1:
            head = head.next
        
        return head
            
