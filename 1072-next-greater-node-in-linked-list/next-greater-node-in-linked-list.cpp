class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {

        
        ListNode* curr = head;
        ListNode* prev = nullptr;

        while (curr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }

        stack<int> st;
        vector<int> ans;

        ListNode* temp = prev;

        while (temp) {

            while (!st.empty() && st.top() <= temp->val) {
                st.pop();
            }

            if (st.empty())
                ans.push_back(0);
            else
                ans.push_back(st.top());

            st.push(temp->val);

            temp = temp->next;
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};