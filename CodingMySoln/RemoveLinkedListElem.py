#1. Talk about examples at high level thinking
#Ask about assumptions from given ds
#empty linked list, check head if null
#ex 1: [1, 1, 1, 1] val = 1
# 0 -> []
#output: []
#ex 2: 0 -> [2, 3] val = 1
#output: [2, 3]
#ex 3: [1,2,3,4] val = 0
#output: [1,2,3,4]
# ex [0,0,0,1,1,1,2,3] -> prev = 3
#2. Describe algorithm and complexities and ask about what type of output we should give (might affect space complexity)
#modifiying in place for spaec complexity or making a new list... ask about both
#3. Type of linked list or DS given, talk about it moer in depth(be aggresive when asking questions)
#safely ask about assumptions to get the better hand 
#for linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr != None:
            if curr.val == val:
                prev.next = curr.next
            elif curr.val != val:
                prev = curr
            curr = curr.next
            
        return dummy.next
Sol = Solution()
head = ListNode()
Sol.removeElements()
#For loop implementation of LinkedList
# class Solution:
#     def removeElements(self, head: ListNode, target: int) -> ListNode:
#         # this is a trick that you can use
#         # a previous node that is before the head
#         # to handle any cases where you remove the 'head'
        
#         #  ret -> 1 -> 2-> 1 -> None (goal: remove 1)
#         #  ret -> 2->1 (after we remove all the 1's)
#         #         ^
#         #         curr ( so we need to fix the tail)
#         # return whatever is after ret
        
#         # idea is just iterate through the list and only take nodes
#         # that isnt equal to the target
        
#         ret = curr = ListNode(0)
#         for node in iter_list(head):
#             if node.val != target:
#                 curr.next = node
#                 curr = curr.next
            
#         curr.next = None
#         return ret.next
    
# def iter_list(node):
#     while node:
#         yield node
#         node = node.next