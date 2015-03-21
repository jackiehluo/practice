Node* Reverse(Node* head)
{
    if(head == NULL)
        return head;
    Node* cur = head;
    Node* temp;
    while(cur != NULL)
    {
        temp = cur->next;
        cur->next = cur->prev;
        cur->prev = temp;
        if(temp == NULL)
            head = cur;
        cur = temp;
    }
    return head;
}