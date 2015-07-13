#include <iostream>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int n(s.length() - 1), ind(n);

    for (int i = 0; i < n; i++)
        if ((s[i] - '0') % 2 == 0)
        {
            ind = i;
            if (s[n] > s[i])
                break;
        }

    if (n == ind)
        cout << -1 << endl;
    else
    {
        swap(s[ind], s[n]);
        cout << s << endl;
    }

    return 0;
}
