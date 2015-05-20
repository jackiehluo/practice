int FindMergeNode(Node *headA, Node *headB)
{
    Node *curA = headA;
    Node *curB = headB;
    int lenA = 0, lenB = 0;
    
    while(curA != NULL)
    {
        curA = curA->next;
        lenA++;
    }
    
    while(curB != NULL)
    {
        curB = curB->next;
        lenB++;
    }
    
    curA = headA;
    curB = headB;
    int diff;
    
    if(lenA > lenB)
    {
        diff = lenA - lenB;
        while(diff--)
            curA = curA->next;
    }
    else if(lenB > lenA)
    {
        diff = lenB - lenA;
        while(diff--)
            curB = curB->next;
    }
    
    while(curA != curB)
    {
        curA = curA->next;
        curB = curB->next;
    }
    
    return curA->data;
}