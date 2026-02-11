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
    ListNode* deleteDuplicates(ListNode* head) {
        
        if(head == NULL) return head;

        ListNode* temp = head;
        ListNode* temp2 = head->next;

        ListNode* list3 = new ListNode(0); 
        ListNode* tail = list3;

        while(temp2 != NULL){

            if(temp->val != temp2->val){
                tail->next = temp;
                tail = tail->next;

                temp = temp2;
                temp2 = temp2->next;
            }
            else{
                
                while(temp2 != NULL && temp->val == temp2->val){
                    temp = temp2;
                    temp2 = temp2->next;
                }

                
                temp = temp2;
                if(temp2 != NULL)
                    temp2 = temp2->next;
            }
        }

        
        if(temp != NULL){
            tail->next = temp;
            tail = tail->next;
        }

        tail->next = NULL;  

        return list3->next;
    }
};
