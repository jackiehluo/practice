#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int f[n], s(0);

    for (int i = 0; i < n; i++)
        cin >> f[i];

    sort(f, f + n);

    for (int i = n - 1; i >= 0; i -= k)
        s += (f[i] - 1) * 2;

    cout << s << endl;
    return 0;
}