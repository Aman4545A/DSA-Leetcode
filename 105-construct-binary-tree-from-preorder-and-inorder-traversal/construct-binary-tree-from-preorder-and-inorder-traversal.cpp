class Solution {
public:
    unordered_map<int, int> mp;

    TreeNode* helper(vector<int>& preorder, int &preIdx, int left, int right) {
        if (left > right)
            return NULL;

        TreeNode* root = new TreeNode(preorder[preIdx]);

        int inIdx = mp[preorder[preIdx]];
        preIdx++;

        root->left = helper(preorder, preIdx, left, inIdx - 1);
        root->right = helper(preorder, preIdx, inIdx + 1, right);

        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {

        for (int i = 0; i < inorder.size(); i++)
            mp[inorder[i]] = i;

        int preIdx = 0;

        return helper(preorder, preIdx, 0, inorder.size() - 1);
    }
};