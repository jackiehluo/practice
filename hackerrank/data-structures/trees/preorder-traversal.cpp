#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <stack>

void Preorder(node *root) {
    if (root == NULL)
        return;
    stack<node *> n;
    n.push(root);
    while (!n.empty())
    {
        struct node *node = n.top();
        cout << node->data << " ";
        n.pop();
        if (node->right)
            n.push(node->right);
        if (node->left)
            n.push(node->left);
    }
}