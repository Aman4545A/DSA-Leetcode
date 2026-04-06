class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        ListNode dummy(0);
        dummy.next = head;

        ListNode* slow = &dummy;

        
        for (int i = 0; i < left - 1; i++) {
            slow = slow->next;
        }

        ListNode* curr = slow->next;
        ListNode* prev = NULL;
        ListNode* next = NULL;


        for (int i = 0; i < right - left + 1; i++) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        slow->next->next = curr; 
        slow->next = prev;       

        return dummy.next;
    }
};