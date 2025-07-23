/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {

        ListNode *slow,*fast;
        slow=head;
        fast=head;

        while(fast && fast->next)
        {
          //update slow&fast pointer first
            slow=slow->next;
            fast=fast->next->next;
            // check if the pointers are equal
            if (slow == fast)
            {
                return true;
            }
                
        }
        // no loop
        return false;
        
    }
};
