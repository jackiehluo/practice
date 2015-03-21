void ReversePrint(Node *head)
{
    if(head != NULL && head->next != NULL)
    {
        Node *prev = NULL;
        Node *cur = head;
        Node *next;
        while(cur != NULL)
        {
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        head = prev;
        cur = head;
        while(cur != NULL)
        {
            cout << cur->data << endl;
            cur = cur->next;
        }
    }
}