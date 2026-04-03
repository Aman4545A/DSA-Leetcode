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
    ListNode* swapPairs(ListNode* head) {
          if (!head || !head->next) return head;

        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* prev = dummy;

        while(prev->next && prev->next->next){
            ListNode* slow = prev->next;
            ListNode* fast = slow->next;

            slow->next = fast->next;
            fast->next = slow;

            prev->next = fast;

            prev = slow;
            
        }

        return dummy->next;
    }
};