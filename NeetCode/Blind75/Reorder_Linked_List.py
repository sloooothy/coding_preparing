# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr=[]
        tmp=head

        while (tmp):
            arr.append(tmp)
            tmp=tmp.next

        l,r=0,len(arr)-1
        # 處理head
        tmp = arr[l]
        l += 1 # 因為 L0 已經作為起點，將左指標向右移動，指向下一個左側節點 (L1)。

        # 使用 while 迴圈交替連接左右兩端的節點。
        # 迴圈會持續，直到 l 指標越過或與 r 指標相遇（表示所有節點都已處理完畢）。
        while l <= r:
            # 處理右邊
            tmp.next = arr[r]
            tmp = tmp.next
            r -= 1 

            # 檢查所有節點是否都已連接完畢，或者只剩下中間一個節點。
            # 如果 l 已經大於 r，表示已處理完所有配對的節點，可以跳出迴圈。
            if l > r:
                break

            # 處理左邊
            tmp.next = arr[l]
            tmp = arr[l]
            l += 1 

        # 迴圈結束後，最後一個連接的節點  的 next 必須設為 None。
        # 這能正確地終止重新排序後的鏈結串列，防止形成循環。
        tmp.next = None
        
                