#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <stack>

void Postorder(node *root) {
    stack<node *> n;
    stack<node *> m;
    n.push(root);
    while (!n.empty())
    {
        node *cur = n.top();
        n.pop();
        m.push(cur);
        if (cur->left)
            n.push(cur->left);
        if (cur->right)
            n.push(cur->right);
    }
    while (!m.empty())
    {
        node *cur = m.top();
        m.pop();
        cout << cur->data << " ";
    }
}
