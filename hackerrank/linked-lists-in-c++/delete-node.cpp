Node* Delete(Node *head, int position)
{
    Node *cur = head;
    Node *prev = NULL;
    for(int i = 0; i < position; i++)
    {
        prev = cur;
        cur = cur->next;
    }
    if(position > 0)
        prev->next = cur->next;
    else
        head = head->next;
    free(cur);
    return head;
}