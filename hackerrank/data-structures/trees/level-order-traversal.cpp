#include <queue>

void LevelOrder(node* root)
{
    queue<node*> q;
    if (root) q.push(root);
    while (!q.empty())
    {
        node* cur = q.front();
        cout << cur->data << " ";
        q.pop();
        if (cur->left) q.push(cur->left);
        if (cur->right) q.push(cur->right);
    }
}