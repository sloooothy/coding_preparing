/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *cur=new ListNode(0);
        ListNode *head=cur; // ❌ 錯誤 1：指標未初始化！
                            // cur 目前是野指標（Uninitialized Pointer），
                            // 直接拿它當 head，後續對 cur->next 解指標會造成 Memory Limit Exceeded 或 Runtime Error。
                            // 提示：通常會使用 Dummy Node（虛擬頭節點），例如 new ListNode(0)。

        int carry=0;
        int sum=0;
        while(l1||l2||carry>0)       // ❌ 錯誤 2：迴圈條件太嚴格！
        {                   // 1. 如果兩個串列長度不同（例如 l1 有 5 個節點，l2 只有 3 個），
                            //    當 l2 走完時迴圈就停了，剩下的 l1 節點完全沒處理到。
                            // 2. 如果兩個串列都走完了，但最後還留有一個進位（carry > 0），
                            //    （例如 5 + 5 = 10），這個進位會被漏掉。
                            // 提示：迴圈條件應該要能持續處理「只要 l1 還在、l2 還在、或還有 carry」的情況。
            sum=0;
            if(l1)
            {
                sum+=l1->val;
                l1=l1->next;
            }
            if(l2)
            {
                sum+=l2->val;
                l2=l2->next;
            }
            if(carry>0)
            {
                sum+=carry;
            }
            carry=sum/10; 
                            // ❌ 錯誤 3：計算順序導致 carry 被拿錯的資料計算！
                            // 上一行你已經改變了 sum 的值，但這裡沒問題；
                            // 真正的問題是：如果在 compute carry 之前/之後沒有先算好當前總和，
                            // 或是寫成 carry = (l1->val + l2->val + carry) / 10 時，
                            // 要注意前一行的 carry 是否已經被覆蓋（雖然這裡 sum 沒影響 carry，但邏輯容易混淆）。
                            // 建議：先算當前總和 current_sum = val1 + val2 + carry，
                            // 再分別用 current_sum 去算新節點的值 (%10) 與新的進位 (/10)。

            cur->next=new ListNode(sum%10); //❌ 錯誤 4：sum未取個位數
            cur=cur->next;
        }


        return head->next;
        
    }
};
