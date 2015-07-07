#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int c[n], l(0), r(n - 1), s(0), d(0), t(0);

    for (int i = 0; i < n; i++)
        cin >> c[i];

    while (l < r + 1)
    {
        t++;
        if (c[l] > c[r])
        {
            if (t % 2)
                s += c[l];
            else
                d += c[l];
            l++;
        }
        else
        {
            if (t % 2)
                s += c[r];
            else
                d += c[r];
            r--;
        }
    }

    cout << s << " " << d << endl;
    return 0;
}
