class Solution {
public:

    ListNode* reverse(ListNode* head){
        ListNode* curr = head;
        ListNode* prev = NULL;

        while(curr){
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    ListNode* doubleIt(ListNode* head) {
        head = reverse(head);

        int carry = 0;
        ListNode* curr = head;

        while (curr) {
            int total = curr->val * 2 + carry;
            curr->val = total % 10;
            carry = total / 10;

            if (curr->next == NULL && carry > 0) {
                curr->next = new ListNode(carry);
                // carry = 0;
                break;
            }

            curr = curr->next;
        }

        return reverse(head);
    }
};