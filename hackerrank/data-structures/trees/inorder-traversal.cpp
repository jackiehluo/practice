#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <stack>

void Inorder(node *root) {
    node *cur = root;
    stack<node *> n;
    while (true)
    {
        if (cur != NULL)
        {
            n.push(cur);
            cur = cur->left;
        }
        else
        {
            if (!n.empty())
            {
                cur = n.top();
                n.pop();
                cout << cur->data << " ";
                cur = cur->right;
            }
            else
                break;
        }
    }
}
