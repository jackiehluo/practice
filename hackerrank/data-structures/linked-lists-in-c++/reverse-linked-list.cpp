Node* Reverse(Node *head)
{
    if(head == NULL || head->next == NULL)
        return head;
    else
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
        return head;
    }
}