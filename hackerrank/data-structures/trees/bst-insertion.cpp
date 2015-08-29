node * insert(node * root, int value)
{
    if (value < root->data)
        if (!root->left)
        {
            node* n = new node;
            n->data = value;
            root->left = n;
        }
        else insert(root->left, value);
    else if (value > root->data)
        if (!root->right)
        {
            node* n = new node;
            n->data = value;
            root->right = n;
        }
        else insert(root->right, value);
   return root;
}