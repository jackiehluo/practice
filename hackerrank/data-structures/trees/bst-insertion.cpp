node* insert(node*& root, int value)
{
    if (root) insert(value < root->data ? root->left : root->right, value);
    else root = new node, root->data = value;
    return root;
}