# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merge_lists=[] # each epoch reset the merge_lists to empty to maintain new merge result of lists
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=None
                # check if l2 existed
                if(i+1)<len(lists):
                    l2=lists[i+1] 
                    
                merge_lists.append(self.mergeList(l1, l2)) 

            lists=merge_lists
        return lists[0]

    def mergeList(self, l1,l2):
        dummy=ListNode()
        tail=dummy
        while l1 and l2:
            # add l1 or l2 (smaller value) to tail
            if l1.val < l2. val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next #move tail to next
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2

        return dummy.next # the dummy head
