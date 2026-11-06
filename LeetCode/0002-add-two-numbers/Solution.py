# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(10)
        curr = dummy
        carry =0
        while l1 or l2:
            total=carry
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            carry=total // 10
            digit=total % 10
            curr.next=ListNode(digit)
            curr=curr.next
        if carry:
            curr.next=ListNode(carry)
        return dummy.next


