Node* MergeLists(Node *headA, Node* headB)
{
    if(headA == NULL)
        return headB;
    else if(headB == NULL)
        return headA;
    else
    {
        if(headA->data < headB->data)
        {
            headA->next = MergeLists(headA->next, headB);
            return headA;
        }
        else
        {
            headB->next = MergeLists(headB->next, headA);
            return headB;
        }
    }
}