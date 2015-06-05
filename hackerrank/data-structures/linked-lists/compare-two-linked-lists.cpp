int CompareLists(Node *headA, Node* headB)
{
    Node *a = headA;
    Node *b = headB;
    while(a != NULL && b != NULL)
    {
        if(a->data == b->data)
        {
            a = a->next;
            b = b->next;
        }
        else
            return 0;
    }
    if(a == NULL && b == NULL)
        return 1;
    else
        return 0;
}