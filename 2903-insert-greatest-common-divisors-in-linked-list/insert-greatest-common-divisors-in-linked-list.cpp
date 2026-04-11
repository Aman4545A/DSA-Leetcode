class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* curr = head;
         
        while (curr != NULL && curr->next != NULL) {
            int getmin = __gcd(curr->val, curr->next->val);
            ListNode* newnode = new ListNode(getmin);

            newnode->next = curr->next;
            curr->next = newnode;

            curr = newnode->next;
        }
        return head;
    }
};