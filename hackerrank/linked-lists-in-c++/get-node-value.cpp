int GetNode(Node *head,int positionFromTail)
{
    Node *cur = head;
    int size = 0;
    while(cur->next != NULL)
    {
        cur = cur->next;
        size++;
    }
    int p = size - positionFromTail;
    cur = head;
    for(int i = 0; i < p; i++)
    {
        cur = cur->next;
    }
    return cur->data;
}