#Talk about examples at a high level
# ex 1. [1, 2, 3, 4] , [5, 6, 7 ,8]
# output: [1,2,3,4,5,6,7,8]
#ex 2. [1,3,7] [0,2, 5]
#output: [0,1,2,3,5,7]
#ex 3. [1, 2, 3] , [1,2,3]
#output: [1, 1, 2, 2, 3, 3]
#ex 4. [1 , 2, 3] [-12 , -11, -5]
#output: [-12, -11 , -5, 1, 2 ,3]
#Assumptions from given ds: only given next node? are we given a previous pointer? what type of linked list 
#are we assuming to have? Circular or acyclic?
#(using Merging of merge sort idea)
#Algorithm? Brute 
#Space Complexity: O(1) in place, Time Complexity: O(N)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
 
        dummy = ListNode(0, None)
        #dummy.next = head
        curr = dummy
        while l1 != None and l2 != None:
        	if l1.val < l2.val:
        		curr.next = l1
        		cur = curr.next
        		l1 = l1.next
        	else:
        		curr.next = l2
        		cur = cur.next
        		l2 = l2.next
        while l1 != None:
        	curr.next = l1
        	curr = curr.next
        	l1 = l1.next
        while l2 != None:
        	curr.next = l2
        	curr = curr.next
        	l2 = l2.next
        return dummy.next







