#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, l, r;
    cin >> n >> l;
    int p[n];

    for (int i = 0; i < n; i++)
        cin >> p[i];

    sort(p, p + n);
    r = max(p[0], l - p[n - 1]) * 2;

    for (int i = 0; i < n - 1; i++)
        r = max(r, p[i + 1] - p[i]);

    cout.precision(20);
    cout << fixed << r / 2.0 << endl;
    return 0;
}
