void Print(Node *head)
{
    Node *a = head;
    while(a != NULL)
    {
        cout << a->data << endl;
        a = a->next;
    }
}