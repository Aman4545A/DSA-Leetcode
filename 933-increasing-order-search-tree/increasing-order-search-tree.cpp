/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* dummy = new TreeNode(0);
    TreeNode* prev = dummy;

    void inorder(TreeNode* root) {
        if (root == NULL) {
            return;
        }

        TreeNode* right = root->right;

        inorder(root->left);

        root->left = NULL;
        prev->right = root;
        prev = root;

        inorder(right);
    }

    TreeNode* increasingBST(TreeNode* root) {
        if (root == NULL) {
            return NULL;
        }

        inorder(root);

        return dummy->right;
    }
};