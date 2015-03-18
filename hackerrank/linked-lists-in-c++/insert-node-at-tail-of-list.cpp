Node* Insert(Node *head, int data)
{
    Node *cur = head;
    Node *add = new Node;
    add->data = data;
    add->next = NULL;
    if(head == NULL)
        head = add;
    else
    {
        while(cur->next != NULL)
        cur = cur->next;
        cur->next = add;
    }
    return head;
}