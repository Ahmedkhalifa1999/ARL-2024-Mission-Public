#include <iostream>
using namespace std;

/* A binary tree node has key, pointer to left child
and a pointer to right child */
struct Node
{
    int key;
    struct Node *left, *right;
};

/* Allocates a new node with the
  given key and NULL left and right pointers. */
struct Node* newnode(int key)
{
    struct Node* node = new (struct Node);
    node->key = key;
    node->left = node->right  = NULL;
    return (node);
}

// Function to find node with minimum absolute
// difference with given K 
// min_diff         --> minimum difference till now
// min_diff_key     --> node having minimum absolute
//                      difference with K
void findMinDiff(struct Node *ptr, int k, int &min_diff,
                                      int &min_diff_key)
{
    if (ptr == NULL)
        return ;

    // If k itself is present
    if (ptr->key == k)
    {
        min_diff_key = 0;
        return;
    }

    // update min_diff and min_diff_key by checking
    // current node value
    int diff = abs(ptr->key - k);
    if (min_diff < diff)
    {
        min_diff = diff;
        min_diff_key = ptr->key;
    }

    // if k is less than ptr->key then move in
    // left subtree else in right subtree
    if (k < ptr->key)
        findMinDiff(ptr->left, k, min_diff, min_diff_key);
    else
        findMinDiff(ptr->right, k, min_diff, min_diff_key);
}

int findClosest(Node *root, int k)
{
    // Initialize minimum difference
    int min_diff = INT32_MAX, min_diff_key = -1;

    // Find value of min_diff_key (Closest key
    // in tree with k)
    findMinDiff(root, k, min_diff, min_diff_key);

    return min_diff_key;
}

// Driver program to run the case
int main()
{
    struct Node *root = newnode(9);
    root->left    = newnode(4);
    root->right   = newnode(17);
    root->left->left = newnode(3);
    root->left->right = newnode(6);
    root->left->right->left = newnode(5);
    root->left->right->right = newnode(7);
    root->right->right = newnode(22);
    root->right->right->left = newnode(20);
    
    int k = 18; // Input value to be searched in BST 

    cout << "Tree: \n\n";
    cout << "     9\n";
    cout << "    /  \\\n";
    cout << "   4    17\n";
    cout << "  / \\     \\\n";
    cout << " 3   6     22\n";
    cout << "    / \\    /\n";
    cout << "   5   7  20\n";
    cout << '\n';
    cout << "---------------------\n";
    cout << "Closest value to " << k << " is: ";
    cout << findClosest(root, k) << '\n'; // Output should be 17
    
    return 0;
}
