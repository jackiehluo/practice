void traverse_left(node * cur)
{
    if (cur)
    {
        traverse_left(cur->left);
        cout << cur->data << " ";
    }
}

void traverse_right(node * cur)
{
     if (cur)
     {
         cout << cur->data << " ";
         traverse_right(cur->right);
     }  
} 

void top_view(node * root)
{
    if (root)
    {
        traverse_left(root->left);
        cout << root->data << " ";
        traverse_right(root->right);
    }
}