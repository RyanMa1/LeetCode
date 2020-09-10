# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, None)
        prev = None
        while head != None:
            temp = head 
            head = head.next  
            temp.next = prev
            prev = temp
        return prev
#examples: [1, 2, 3, 4, 5]
#output: 5,4,3,2,1
#Assumptions: we are not modifying anything simply iterating throughout list, linked list is not a cycle? acyclic
#Time Complexity: O(n)
#Space Complexity: O(n)
#what type of output do we want? an array or linked list?

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Sol = Solution()
head = Sol.reverseList(node1)
cur = head
while cur != None:
    print(cur.val)
    cur = cur.next