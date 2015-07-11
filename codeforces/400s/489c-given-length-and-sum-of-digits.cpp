#include <iostream>
using namespace std;

int main()
{
    int m, s, t, i;
    cin >> m >> s;
    string a, b;

    if (s == 0)
    {
        cout << (m == 1 ? "0 0" : "-1 -1") << endl;
        return 0;
    }

    for (i = 0; i < m; i++)
    {
        t = min(s, 9);
        b += t + '0';
        s -= t;
    }

    if (s > 0)
    {
        cout << "-1 -1" << endl;
        return 0;
    }

    for (i = m - 1; i >= 0; i--)
        a += b[i];

    for (i = 0; a[i] == '0'; i++);

    a[i]--, a[0]++;
    cout << a << " " << b << endl;
    return 0;
}