#include <iostream>

// Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int count = 0;
    int countNodes(TreeNode* root) {
        if(root != nullptr){
            count++;
            countNodes(root->left);
            countNodes(root->right);
        }
        return count;
    }
    //InOrder traversal where you visit left subtree, root node, then right subtree

};
int main(){
    TreeNode test(2);
    TreeNode left(3);
    TreeNode right(1);
    test.left = &left;
    test.right = &right;
    Solution sol;
    std::cout << sol.countNodes(&test);

    return 0;
}