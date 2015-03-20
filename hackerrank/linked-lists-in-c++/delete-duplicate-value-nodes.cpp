Node* RemoveDuplicates(Node *head)
{
    Node *cur = head;
    while(cur->next != NULL)
    {
        if(cur->data == (cur->next)->data)
        {
            if(cur == head)
                head->next = (head->next)->next;
            else
                cur->next = (cur->next)->next;
        }
        else
            cur = cur->next;    
    }
    return head;
}