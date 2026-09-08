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

        // 宣告 Hash Map：用來建立「舊節點記憶體位址 -> 新節點記憶體位址」的對照表
        // Key: 舊 Node 的指標
        // Value: 剛 new 出來對應的新 Node 指標
        unordered_map<Node*, Node*> old_to_new;
        // 步驟一：第一遍走訪舊串列，單純為每一個舊節點建立一個「新節點」
        Node* cur = head;
        while (cur != nullptr) {
            // 複製舊節點的 val，建立全新節點
            // 存入 Map 進行對照，此時新節點的 next 和 random 都還是預設的 NULL
            old_to_new[cur] = new Node(cur->val);
            // 移動到下一個舊節點
            cur = cur->next;
        }
        // -------------------------------------------------------------
        // 步驟二：請嘗試在這裡自己實作！
        // 提示：
        // 1. 重新讓 cur = head (從頭走訪舊串列)
        cur=head;
        // 2. 在迴圈中，利用 Map 尋找對應的新節點：
        while(cur)
        {
            //    - 新節點的 next   = old_to_new[cur->next]
            //    - 新節點的 random = old_to_new[cur->random]
            old_to_new[cur]->next=old_to_new[cur->next];
            old_to_new[cur]->random=old_to_new[cur->random];

            // 3. 移動 cur，直到走訪結束
            cur=cur->next;

        }

        // -------------------------------------------------------------

        // 步驟三：回傳「舊 head 映射出的新 head」
        return old_to_new[head];
        
    }
};
