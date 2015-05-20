Node* Insert(Node *head, int data)
{
    Node *add = new Node;
    add->data = data;
    add->next = head;
    head = add;
    return head;
}