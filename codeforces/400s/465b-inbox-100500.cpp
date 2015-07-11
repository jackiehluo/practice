#include <iostream>
using namespace std;

int main()
{
    int n, t, l(0), c(0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> t;
        if (t == 1)
            c++;
        else if (l == 1)
            c++;
        l = t;
    }

    c += l;
    if (c > 0)
        cout << c - 1 << endl;
    else
        cout << 0 << endl;
    return 0;
}