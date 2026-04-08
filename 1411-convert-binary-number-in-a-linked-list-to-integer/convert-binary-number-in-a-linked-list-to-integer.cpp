
class Solution {
public:
      ListNode* reverseList(ListNode* head) {
       ListNode* curr = head;
       ListNode* prev = NULL;
       ListNode* next = NULL ;

       while(curr != NULL) {
         next = curr->next;
         curr->next = prev ;
         prev = curr ;
         curr = next;  

       }
       return prev;
    }
    
    int getDecimalValue(ListNode* head) {
        ListNode* temp = reverseList(head);
        int result =0;
        int i =0; 
        while(temp != NULL){
            if(temp->val == 1){
               result = result + pow(2, i);
                temp = temp->next;
                i++;
            }
            else{
                temp = temp->next;
                i++;
            }
        }
        return result;
    }
};