Node* InsertNth(Node *head, int data, int position)
{
    Node *add = new Node;
    add->data = data;
    add->next = NULL;
    
    if(head == NULL)
        head = add;
    else if(position == 0)
    {
        add->next = head;
        head = add;
    }
    else
    {
        Node *cur = head;
        int d = 1;
        while(cur != NULL)
        {
            if(d == position)
            {
                add->next = cur->next;
                cur->next = add;
                break;
            }
            cur = cur->next;
            d++;
        }
    }
    return head;
}