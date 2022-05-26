# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        fast, middle = head, head
        while fast.next != None and fast.next.next != None:
            middle = middle.next
            fast = fast.next.next
                        
        # reverse second portion
        prev, current = None, middle.next
        while current != None:
            tmp = current.next
            current.next = prev
            prev =  current
            current = tmp
        middle.next = None

        # combine both lists
        head1, head2 = head, prev
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp