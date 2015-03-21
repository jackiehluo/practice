int HasCycle(Node* head)
{
    Node* tortoise = head;
    Node* hare = head;
    
    if(head == NULL)
        return 0;
    
    while(true)
    {
        tortoise = tortoise->next;
        if(hare->next != NULL)
            hare = (hare->next)->next;
        else
            return 0;
        if(tortoise == NULL || hare == NULL)
            return 0;
        if(tortoise == hare)
            return 1;
    }
}