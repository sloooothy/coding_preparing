/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // 邊界條件：如果傳進來的串列是空的，直接返回 nullptr
        if (head == nullptr) return nullptr;
        // =========================================================================
        // 步驟一：複製並交錯插隊（Interleave）
        // -------------------------------------------------------------------------
        // 概念：
        // 走訪原本的串列，每遇到一個舊節點 A，就 new 一個新節點 A'，
        // 並將 A' 直接插在 A 的正後方。
        //
        // 結構變化：
        // 原本：A -> B -> C -> nullptr
        // 變成：A -> A' -> B -> B' -> C -> C' -> nullptr
        //
        // 關鍵思考：
        // 這樣做之後，任何一個「舊節點 A 的新節點 A'」，就剛好永遠是「A->next」！
        // 我們直接用實體鏈結關係取代了 Hash Map！
        // =========================================================================
        
        // 【請在此處寫 步驟一 的程式碼】
        Node *cur=head;
        while(cur)
        {
            Node *tmp=new Node(cur->val); //new node
            tmp->next=cur->next;
            cur->next = tmp;
            cur=cur->next->next; //go to next original node
        }


        // =========================================================================
        // 步驟二：設定新節點的 random 指標
        // -------------------------------------------------------------------------
        // 概念：
        // 再次從頭走訪這個交錯串列（只看舊節點 cur）。
        // 如果舊節點 cur 有 random 指向（例如 cur->random 指向 B）：
        // 那麼「新節點 (cur->next)」的 random，就應該指向「B 的新節點 (B->next)」。
        //
        // 邏輯公式：
        // cur->next->random = cur->random->next;
        // （別忘了要先檢查 cur->random 是否為空指標喔！）
        // =========================================================================

        // 【請在此處寫 步驟二 的程式碼】
        cur =head; //reset start
        while(cur) //&&cur->next
        {
            if(cur->random!=nullptr)
            {
                cur->next->random=cur->random->next;
            }
            cur=cur->next->next;
        }


        // =========================================================================
        // 步驟三：拆分串列（Separate / Unweave）
        // -------------------------------------------------------------------------
        // 概念：
        // 目前指標全部都接好了，最後一步是把這條交錯的串列拆回兩條獨立的串列：
        // 1. 還原舊串列：A -> B -> C -> nullptr
        // 2. 提取新串列：A' -> B' -> C' -> nullptr
        //
        // 提示：
        // 記得先用一個指標記錄新串列的頭 (head_new = head->next)，
        // 然後用雙指標（例如 cur 和 copy）一邊向前走，一邊把 next 重新接回正確的軌道上。
        // =========================================================================

        // 【請在此處寫 步驟三 的程式碼】
        // old list
        cur=head;
        // new list
        Node *new_head= head->next;
        Node *copy= new_head;
        while(cur && copy)
        {
            //old list recon
            cur->next=copy->next;
            cur=copy->next;
            //new list recon
            if(copy->next) //check 
            {
                copy->next=cur->next;
                copy=cur->next;
            }
            else
            {
                copy->next=nullptr;
            }
            
        }

        // 最後回傳新串列的頭
        return new_head;
        
    }
};
