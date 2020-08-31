#submitted 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        e1 = head
        e2 = head
        while(e2!=None and e2.next!=None):
            e1=e1.next
            e2=e2.next.next
        print(e1.val)
        return e1
    
        