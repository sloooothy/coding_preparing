# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast,slow=head,head
        cnt_n=0

        for step in range(n):
            fast=fast.next # move fast n forward
            if fast==None:#if remove the first block
                return head.next

        while(fast.next): # check fast.next to see if fast reach the end
            fast=fast.next
            slow=slow.next

        slow.next=slow.next.next #skip the slow's next block

        return head
