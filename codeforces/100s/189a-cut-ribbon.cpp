#include <iostream>
using namespace std;

int main()
{
    int n, a, b, c, r[5000];
    cin >> n >> a >> b >> c;
    r[0] = 1;

    for (int i = 1; i <= n; i++)
    {
        if (i - a >= 0 and r[i - a] > 0)
            r[i] = max(r[i], r[i - a] + 1);
        if (i - b >= 0 and r[i - b] > 0)
            r[i] = max(r[i], r[i - b] + 1);
        if (i - c >= 0 and r[i - c] > 0)
            r[i] = max(r[i], r[i - c] + 1);
    }

    cout << r[n] - 1 << endl;
    return 0;
}