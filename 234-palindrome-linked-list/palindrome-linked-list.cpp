class Solution {
public:
    
    ListNode* copyList(ListNode* head) {
        if (!head) return NULL;
        
        ListNode* newHead = new ListNode(head->val);
        ListNode* temp1 = head->next;
        ListNode* temp2 = newHead;
        
        while (temp1) {
            temp2->next = new ListNode(temp1->val);
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        
        return newHead;
    }
    
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;

        
        ListNode* originalCopy = copyList(head);

        
        ListNode* curr = head;
        ListNode* prev = NULL;
        ListNode* next = NULL;

        while (curr != NULL) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        ListNode* temp1 = prev;           
        ListNode* temp2 = originalCopy;   

        while (temp1 && temp2) {
            if (temp1->val != temp2->val)
                return false;
            temp1 = temp1->next;
            temp2 = temp2->next;
        }

        return true;
    }
};
