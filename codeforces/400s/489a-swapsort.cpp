#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, t(0);
    cin >> n;
    int a[n], s[n], r[n][2];

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        s[i] = a[i];
    }

    sort(s, s + n);

    for (int i = 0; i < n; i++)
        if (a[i] != s[i])
            for (int j = i + 1; j < n; j++)
                if (a[j] == s[i])
                {
                    swap(a[i],a[j]);
                    r[t++][0] = i, r[t - 1][1] = j;
                    break;
                }

    cout << t << endl;

    for (int i = 0; i < t; i++)
        cout << r[i][0] << " " << r[i][1] << endl;

    return 0;
}