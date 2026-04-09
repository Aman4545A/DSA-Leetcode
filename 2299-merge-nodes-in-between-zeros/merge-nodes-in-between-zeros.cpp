class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* temp = head->next;
        ListNode* dummy = new ListNode(0);
        ListNode* temp2 = dummy;
        int sum = 0;
        while(temp!=NULL){
            if(temp->val ==0){
               temp2->next = new ListNode(sum);
               temp2= temp2->next;
               sum = 0;
                
            }else{
            sum = sum + temp->val;
            }
            temp= temp->next;
           
        }
        return dummy->next;
    }
};